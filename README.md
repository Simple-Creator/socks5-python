# SOCKS5 Proxy Server

一个基于Python asyncio的轻量级SOCKS5代理服务器，支持用户名密码认证。

## 使用方法

### 安装

```bash
# 使用pip安装
pip install socks5

# 或者使用uv安装（推荐）
uv add socks5
```

### 启动代理服务器

```bash
# 使用默认参数启动
socks5

# 自定义参数启动
socks5 --host 0.0.0.0 --port 1080 --username myuser --password mypass
```

#### 参数说明

- `--host`: 服务器监听地址，默认为 `0.0.0.0`
- `--port`: 服务器监听端口，默认为 `1080`
- `--username`: 认证用户名，默认为 `admin`
- `--password`: 认证密码，默认为 `admin`

### 客户端配置

在需要使用代理的应用程序中配置以下信息：

- 代理类型：SOCKS5
- 服务器地址：代理服务器所在的主机IP
- 端口：与启动时指定的端口一致（默认1080）
- 用户名：与启动时指定的用户名一致（默认admin）
- 密码：与启动时指定的密码一致（默认admin）

## 开发

### 项目结构

```
socks5/
├── src/
│   └── socks5/
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
# 克隆仓库
git clone https://github.com/yourusername/socks5.git
cd socks5

# 使用uv创建虚拟环境并安装依赖
uv venv
uv pip install -e .

# 安装开发依赖
uv pip install -e ".[dev]"
```

### 运行测试

```bash
# 使用uv运行测试
uv run pytest

# 或者直接使用pytest
pytest
```

## 功能特点

- 基于Python asyncio实现的高性能异步代理服务器
- 支持SOCKS5协议
- 支持用户名密码认证
- 支持IPv4、IPv6和域名目标地址
- 简单易用的命令行接口

## 许可证

MIT License