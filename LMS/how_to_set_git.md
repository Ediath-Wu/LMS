# 在vscode中配置git

## 安装

## 配置git

### 1.设置全局变量

```
git config --global user.name "your name" 
git config --global user.email "your@email.com"
```

### 2.登陆github,创建SSHKey

> ssh-keygen -t rsa -C "your@email.com"

![.ssh](images/1.png)

会在本地用户文件夹下生成.ssh的文件夹，里面包含id_rsa和id_rsa.pub两个文件

![".ssh"](images/2.png)

![id_rsa.pub](images/3.png)

![id_rsa.pub](images/4.png)

然后我们回到刚刚注册的GitHub账号里去，点击设置

![github-setting](images/5.jpg)

![ssh keys](images/6.jpg)

![new ssh key](images/7.jpg)

![add ssh key](images/8.jpg)

然后回到git，输入

`ssh -T git@github.com`

最后，输入yes!

![成功](images/9.png)

### 3.克隆仓库

复制GitHub上的仓库地址

![复制GitHub上的仓库地址!](images/10.jpg)

在Git上输入这个，克隆仓库到本地

```text
git clone git@github.com:fenyukuang/TestCode.git
```


![git clone](images/11.png)

然后把我们一遍文章中生成的VScode的配置文件复制过去。
![复制配置文件](images/12.png)
