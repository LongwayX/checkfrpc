# checkfrpc
scripts for checking frpc service on ubuntu
这个脚本就是自己写来确保每次重启frpc服务启动成功的，防止连接不到服务器
# Usage
## 安装frpc
参考此[文章](https://blog.csdn.net/Zhy_201810576/article/details/124546567)
## 下载并修改文件
运行以下指令
~~~bash
  git clone https://github.com/longwayfather/checkfrpc.git
  cd checkfrpc
  vi checkfrpc.service   
~~~
  修改 line 10
~~~bash
ExecStart=/usr/bin/python /root/checkfrpc/checkfrpc.py 
~~~
其中/usr/bin/python 修改为自己本地python安装的位置，如不知道可以使用如下命令
~~~bash
whereis python
~~~
用获取结果中任意一个路径替换/usr/bin/python。（python2\python3皆可）此外，还需更改/root/checkfrpc/checkfrpc.py 为下载的checkfrpc.py的绝对位置
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
以上基于Ubuntu20.04系统，（在centos7上测试成功）另外为了不浪费系统资源，checkfrpc服务会在25分钟后关闭，属正常现象。
