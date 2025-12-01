# MobaXterm Pro KeyGen

MobaXterm Pro KeyGen 是一个基于 Python Flask 的 Web 工具，用于在网页端生成 MobaXterm Professional 版本的许可证密钥。

## 免责声明
**本项目仅用于个人学习和测试目的，禁止用于任何商业用途。请支持正版软件！**

## 项目信息
*   **作者**: Reyanmatic
*   **版本**: 1.0.0
*   **GitHub**: [https://github.com/iHub-2020/Mobaxterm_pro](https://github.com/iHub-2020/Mobaxterm_pro)

## 🖼️ 界面预览 | UI Preview

<p align="center">
  <img src="UI.png" alt="MobaXterm KeyGen UI" width="600">
</p>

---

## 本地启动 (Python 环境)

如果您在本地电脑（Windows/Mac/Linux）上已安装 Python 3 环境，可直接运行：

1.  **安装依赖**
    ```bash
    pip install --no-cache-dir -r requirements.txt
    ```

2.  **启动服务**
    ```bash
    python app.py
    ```

3.  **访问**
    打开浏览器访问：`http://localhost:5000`

---

## Docker 部署教程 (Debian / Ubuntu)

如果您希望在服务器上通过 Docker 部署，请参考以下步骤。本教程假设您使用的是 Debian 或 Ubuntu 系统。

### 准备工作：安装 Docker

如果您的服务器尚未安装 Docker，请执行以下命令进行安装：

```bash
# 更新软件源
sudo apt-get update

# 安装 Docker
curl -fsSL https://get.docker.com | bash

# 启动 Docker 并设置为开机自启
sudo systemctl start docker
sudo systemctl enable docker

部署方式一：手动构建镜像 (Docker Run)
这种方式适合快速测试，无需额外的配置文件。

克隆项目代码

bash
git clone https://github.com/iHub-2020/Mobaxterm_pro.git
cd Mobaxterm_pro

构建 Docker 镜像
在项目目录下执行以下命令，将镜像命名为 mobaxterm-keygen：

bash
docker build -t mobaxterm-keygen .

运行容器
后台运行容器，并将服务器的 5000 端口映射到容器内部：

bash
docker run -d -p 5000:5000 --name mobaxterm-gen --restart always mobaxterm-keygen

访问
在浏览器中输入 http://服务器IP:5000 即可访问。

部署方式二：使用 Docker Compose (推荐)
这种方式更易于管理和维护。

安装 Docker Compose 插件

bash
sudo apt-get update
sudo apt-get install docker-compose-plugin

获取项目

bash
git clone https://github.com/iHub-2020/Mobaxterm_pro.git
cd Mobaxterm_pro

创建 docker-compose.yml 文件
在项目根目录下创建一个名为 docker-compose.yml 的文件：

bash
nano docker-compose.yml

并将以下内容粘贴进去：

yaml
version: '3'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    container_name: mobaxterm-gen
    restart: always

(按 Ctrl+O 保存，按 Ctrl+X 退出)

启动服务

bash
docker compose up -d

停止或更新

停止服务：docker compose down
更新代码后重新构建：docker compose up -d --build
使用方法
打开部署好的网页。
在 姓名 栏输入任意名称。
在 版本 栏输入您的 MobaXterm 版本号 (例如 25.0, 24.2)。
点击 生成密钥 按钮。
浏览器会自动下载一个名为 Custom.mxtpro 的文件。
激活：将下载的文件直接放入 MobaXterm 软件的安装目录（即 MobaXterm.exe 所在的文件夹），重启软件即可。
致谢
核心算法参考自：https://github.com/flygon2018/MobaXterm-keygen
