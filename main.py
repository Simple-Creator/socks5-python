import asyncio
import socket
from argparse import ArgumentParser
from asyncio import StreamReader, StreamWriter


class Socks5ProxyServer:
    def __init__(self, local_addr, local_port, username, password):
        self.local_addr = local_addr
        self.local_port = local_port
        self.username = username
        self.password = password

    async def handshake(self, reader, writer):
        sub_data = await reader.read(2)
        sub_ver, ulen = sub_data

        uname = await reader.read(ulen)
        uname = uname.decode()

        plen = await reader.read(1)
        plen = int.from_bytes(plen, byteorder="big")

        passwd = await reader.read(plen)
        passwd = passwd.decode()

        if self.username == uname and passwd == self.password:
            response = bytes([1, 0])
            writer.write(response)
            return True
        else:
            response = bytes([1, 10])
            writer.write(response)
            return False

    async def handle_client(self, reader: StreamReader, writer: StreamWriter):

        try:
            data = await reader.read(20)
            ver, nmethods, methods = data
            if ver != 5:
                return

            response = bytes([5, 2])
            writer.write(response)

            flag = await self.handshake(reader, writer)
            if not flag:
                return

            data = await reader.read(4)
            ver, cmd, _, atyp = data
            if ver != 5 or cmd != 1:
                return

            if atyp == 1:  # IPv4
                addr = socket.inet_ntop(socket.AF_INET, await reader.read(4))
            elif atyp == 3:  # 域名
                domain_length_1 = await reader.read(1)
                domain_length = (domain_length_1)[0]
                addr = await reader.read(domain_length)
                addr = addr.decode()
            elif atyp == 4:  # IPv6
                addr = socket.inet_ntop(socket.AF_INET6, await reader.read(16))
            else:
                return

            port = int.from_bytes(await reader.read(2), 'big', signed=False)

            remote_reader, remote_writer = await asyncio.open_connection(addr, port)

            writer.write(b'\x05\x00\x00\x01\x00\x00\x00\x00\x00\x00')

            tasks = [
                asyncio.create_task(self.transfer(reader, remote_writer)),
                asyncio.create_task(self.transfer(remote_reader, writer))
            ]

            await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

        except Exception as e:
            print(f"Error: {e}")
        finally:
            writer.close()

    async def transfer(self, reader, writer):
        try:
            while not reader.at_eof():
                data = await reader.read(4096)
                writer.write(data)
                await writer.drain()
        finally:
            writer.close()

    async def start(self):
        server = await asyncio.start_server(self.handle_client, self.local_addr, self.local_port)
        print(f"Serving on {self.local_addr}:{self.local_port}")
        try:
            await server.serve_forever()
        except KeyboardInterrupt:
            server.close()


if __name__ == "__main__":
    parser = ArgumentParser(description="Async Socks5 Proxy")
    parser.add_argument("--host", default="0.0.0.0", help="host:默认为：0.0.0.0")
    parser.add_argument("--port", default="1080", help="端口:默认为：1080")
    parser.add_argument("--username", default="admin", help="用户名: 默认为：admin")
    parser.add_argument("--password", default="admin", help="密码: 默认为：admin")
    args = parser.parse_args()

    proxy_server = Socks5ProxyServer(args.host, int(args.port), args.username, args.password)
    asyncio.run(proxy_server.start())