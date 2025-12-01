# MobaXterm Pro KeyGen

MobaXterm Pro KeyGen 是一个基于 Python Flask 的 Web 工具，用于在网页端生成 MobaXterm Professional 版本的许可证密钥。

## 免责声明
**本项目仅用于个人学习和测试目的，禁止用于任何商业用途。请支持正版软件！**

## 项目信息
*   **作者**: Reyanmatic
*   **版本**: 1.0.0
*   **GitHub**: [https://github.com/iHub-2020/Mobaxterm_pro](https://github.com/iHub-2020/Mobaxterm_pro)

## 界面预览 | UI Preview

<p align="center">
  <img src="UI.png" alt="MobaXterm KeyGen UI" width="600">
</p>

---
## Docker 部署教程 (Debian / Ubuntu)
如果您希望在服务器上通过 Docker 部署，请参考以下步骤。本教程假设您使用的是 Debian 或 Ubuntu 系统。

### 准备工作：安装 Docker

如果您的服务器尚未安装 Docker，请执行以下命令进行安装：

```bash
# 更新软件源
sudo apt-get update
```
### 安装 Docker
```bash
curl -fsSL https://get.docker.com | bash
```
### 启动 Docker 并设置为开机自启
```bash
sudo systemctl start docker
sudo systemctl enable docker
```
---

# 构建镜像

### 创建目录(推荐普通用户，权限1000)
```bash
sudo mkdir -p /opt/mobaxterm_pro_keygen/app
```
1. **用 sudo 克隆仓库**
```bash
cd /opt
sudo git clone https://github.com/iHub-2020/mobaxterm_pro_keygen.git
```

2. **将文件夹的所有权修改为你的用户**
```bash
sudo chown -R 1000:1000 /opt/mobaxterm_pro_keygen
sudo chmod -R 755 /opt/mobaxterm_pro_keygen
```

3. **确认一下文件都在**
```bash
ls -l /opt/mobaxterm_pro_keygen
```

4. **构建镜像（注意最后有个点 . 代表当前目录）**
```bash
cd /opt/mobaxterm_pro_keygen/
docker build -t mobaxterm-pro-keygen-image:latest .
```

---
# 部署容器
推荐在Portainer 中通过stack 方式部署：

```yaml
version: '3.8'

services:
  mobaxterm-pro-keygen:
    container_name: mobaxterm-pro-keygen
    image: mobaxterm-pro-keygen-image:latest
    
    volumes:
      - /opt/mobaxterm_pro_keygen/app:/app
      
    ports:
      - "5000:5000"
      
    restart: always
```

---
# 使用方法
* 打开部署好的网页
* 在 姓名 栏输入任意名称
* 在 版本 栏输入您的 MobaXterm 版本号 (例如 25.0, 24.2)
* 点击 生成密钥 按钮
* 浏览器会自动下载一个名为 Custom.mxtpro 的文件
* 激活：将下载的文件直接放入 MobaXterm 软件的安装目录（即 MobaXterm.exe 所在的文件夹），重启软件即可
---

# 致谢
### 核心算法参考自：https://github.com/flygon2018/MobaXterm-keygen
