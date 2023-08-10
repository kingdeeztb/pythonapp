#!/bin/bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH


echo "1.生成服务初始化脚本"

read -p "输入你的创建的服务名称(会初始化一个[servername].service的文件):" servername
touch $servername.service

echo "[Unit]
Description=prometheus
After=network.target

StartLimitIntervalSec=500
StartLimitBurst=20
 
[Service]
Type=simple
WorkingDirectory=/prometheus
ExecStart=/prometheus/prometheus -c /frp/frpc.ini
Restart=on-failure
RestartSec=3s
 
[Install]
WantedBy=multi-user.target" >$servername.service


:<<!
根据需要修改初始化脚本
!
echo "2.接下来根据服务实际情况修改初始化脚本"
#read -p "输入你的创建的服务名称(servername):" servername
read -p "输入你的服务路径[例如:/opt,最后不要有"/"]:" serverpath
read -p "输入你的服务执行命令(最终执行的命令,例如/opt/frp/frpc -c /opt/frp/frpc.ini):" serverexec
sed -i -e "2cDescription='$servername'"  -e "10cWorkingDirectory='$serverpath'" -e "11cExecStart='$serverexec'" $servername.service
echo "全部修改完成,创建服务中..."


cp -a  $servername.service /etc/systemd/system/
chmod +x /etc/systemd/system/$servername.service
sleep 1
systemctl daemon-reload
sleep 1
systemctl enable $servername
sleep 1
systemctl start $servername
systemctl status $servername
echo "服务启动完成."