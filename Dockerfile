# 使用轻量级 Python 镜像
FROM python:3.9-slim

# 一行命令安装 Firefox 和必要的系统工具 (全自动)
RUN apt-get update && apt-get install -y \
    firefox-esr \
    wget \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1 \
    && rm -rf /var/lib/apt/lists/*

# 设置工作目录
WORKDIR /app

# 复制文件并安装 Python 库
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# 启动程序
CMD ["python", "main.py"]
