# Title: MobaXterm Pro KeyGen Dockerfile
# Version: 1.0.1
# Author: Reyanmatic
# Description: Dockerfile to build the MobaXterm KeyGen container.

FROM python:3.9-slim

# 使用 LABEL 替代已废弃的 MAINTAINER 指令
LABEL maintainer="Reyanmatic"
LABEL version="1.0.0"
LABEL description="MobaXterm KeyGen container"

WORKDIR /usr/src/app

COPY requirements.txt ./

# 增加国内源配置（可选，如果构建速度慢可以取消注释下面这行）
# RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./app.py" ]
