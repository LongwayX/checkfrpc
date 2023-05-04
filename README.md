# checkfrpc
scripts for checking frpc service on ubuntu
这个脚本就是自己写来确保每次重启frpc服务启动成功的，防止连接不到服务器
# Usage
## 安装frpc
参考此[文章](https://blog.csdn.net/Zhy_201810576/article/details/124546567)
## 下载并修改文件
运行以下指令
~~~
  git clone https://github.com/longwayfather/checkfrpc.git
  cd checkfrpc
  vi checkfrpc/checkfrpc.service   
~~~
  然后修改 line 13中
  /home/linaro/checkfrpc.sh 
  为自己下载文件checkfrpc.sh 的绝对路径并保存。
  之后
 ~~~
   vi checkfrpc/checkfrpc.sh
 ~~~
 修改line 2中 export PYTHONPATH=/usr/lib/python3/dist-packages 为自己python包的路径(绝对路径)
 不知道自己python安在哪的可以终端输入
 ~~~
  pip3 list # 查看所有已安装的包
  pip3 show ${package} # 查看某个特定的安装包的路径 从而找到自己python包的绝对路径
 ~~~
 修改line4 中/home/linaro/checkfrpc.py 为自己下载的checkfrpc.py的绝对路径
 ## 注册为system服务
 运行以下代码
 ~~~
  cp checkfrpc/checkfrpc.service /etc/systemd/system/
  sudo chmod +x /etc/systemd/system/checkfrpc.service # 修改权限
  sudo systemctl daemon-reload # 重载系统服务
  sudo systemctl enable checkfrpc.service # 开机自启动checkfrpc.service
  sudo systemctl start checkfrpc # 开始运行checkfrpc服务
  sudo systemctl status checkfrpc # 查看checkfrpc服务状态
 ~~~
此时如果出现running(activate) 说明服务启动成功
之后重启，再次查看:
~~~
  sudo systemctl status checkfrpc
~~~
如果出现running(activate) 说明自启动设置成功
# 注意
以上基于Ubuntu20.04系统，另外为了不浪费系统资源，checkfrpc服务会在25分钟后关闭，属正常现象。
