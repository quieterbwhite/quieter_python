# systemctl

```
服务（service）：管理着后台服务；
挂载（mount）自动挂载（automount）：用来挂载文件系统；
目票（target）：运行级别；
套接字（socket）：用来创建套接字，并在访问套接字后，立即利用依赖关系间接地启动另一单位；

systemctl --type=service

systemctl status mongodb.service            // 查看mongodb启动状态
systemctl start mongodb.service             // 启动 mongodb
systemctl stop mongodb.service              // 关闭 mongodb
systemctl enable mongodb.service            // 开机启动 mongodb 服务
systemctl disable mongodb.service           // 开机关闭 mongodb 服务




```




