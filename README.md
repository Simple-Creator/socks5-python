# xsocks5

一个基于Python asyncio的轻量级SOCKS5代理服务器，支持用户名密码认证。

## 使用方法

### 安装

```bash
# 使用pip安装
pip install xsocks5
```

### 服务端启动代理

```bash
# 使用默认参数启动
xsocks5

# 自定义参数启动
xsocks5 --host 0.0.0.0 --port 1080 --username myuser --password mypass
```

#### 参数说明

- `--host`: 服务器监听地址，默认为 `0.0.0.0`
- `--port`: 服务器监听端口，默认为 `1080`
- `--username`: 认证用户名，默认为 `admin`
- `--password`: 认证密码，默认为 `admin`

### 客户端配置
- 浏览器使用Proxy SwitchyOmega 3插件，配置代理服务器
  - 代理类型：SOCKS5
  - 服务器地址：代理服务器所在的主机IP
  - 端口：与启动时指定的端口一致（默认1080）
  - 用户名：与启动时指定的用户名一致（默认admin）
  - 密码：与启动时指定的密码一致（默认admin）
- 也可搭配clash等客户端使用

## 开发

### 项目结构

```
xsocks5/
├── src/
│   └── xsocks5/
│       ├── __init__.py
│       └── main.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── pyproject.toml
└── README.md
```

### 开发环境设置

```bash
# 安装uv
## On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
## On Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# 克隆仓库
git clone https://github.com/Simple-Creator/socks5-python.git
cd socks5-python

# 使用uv创建虚拟环境并安装依赖
uv sync
```

## 功能特点

- 基于Python asyncio实现的高性能异步代理服务器
- 支持SOCKS5协议
- 支持用户名密码认证
- 支持IPv4、IPv6和域名目标地址
- 简单易用的命令行接口

## 许可证

MIT License