#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import platform
from collections import OrderedDict
import time
import sys
import subprocess

def info():
    # 打印系统时间
    # print("==============="+ip_info_text+" 服务系统时间信息===============\n")
    machineTime = "".join(os.popen('date +"%Y-%m-%d %H:%M:%S" ').readlines()).replace("\n", " ")
    print(machineTime)
    # 打印IP信息
    ip_info_text = "".join(os.popen(
        "ifconfig | grep -wo  'inet [0-9]*.[0-9]*.[0-9]*.[0-9]*'|grep -nv '127.0.0.1'").readlines()).replace("\n", " ").replace("inet", "").replace("1: 172.17.0.1 2:","")
    print("===="+ip_info_text+' '+machineTime+" 服务器信息====\n")
    print(ip_info_text)
    # print("==============="+ip_info_text+" 内核信息===============\n")
    print("内核信息："+str(platform.uname()
                      [0]+" "+str(platform.uname()[2])+" "+str(platform.uname()[4])))
    # print("==============="+ip_info_text+" 进程信息===============\n")
    info_process = "".join(os.popen("ps -ef| grep sshd \n").readlines())
    print(info_process)
    # print("==============="+ip_info_text+" 内存信息===============\n")
    info_mem = "".join(os.popen("free -h \n").readlines())
    print(info_mem)
    # print("==============="+ip_info_text+" 硬盘信息===============\n")
    hardDisk = "".join(os.popen("df -h \n").readlines())
    print(hardDisk)
    # print("==============="+ip_info_text+" 磁盘使用率检查结果===============\n")
    database_info="".join(os.popen("df -h \n").readlines())
    print(database_info)
    # 硬盘使用率判断检测
    disk_info_text = "".join(os.popen(
        "df -h| grep -wo '[0-9]*%'|grep   '[0-9]'").readlines()).replace("\n", ",").replace("%", "")
    # 硬盘分区生成数组
    arr = disk_info_text.split(',')
    # 去除硬盘数组空值
    while "" in arr:
        arr.remove("")
    # print(arr)
    # 获取硬盘数组长度
    arr_len = len(arr)
    # print(arr_len)
    # 硬盘使用率超过100%判断
    h = 0
    while h <= (arr_len-1):
        if int(arr[h]) < 70:
            print("通过啦！")
        else:
            print("注意啦!硬盘使用量超过预警值70%,当前值为"+arr[h]+"%.")
        h = h+1

# 将sql语句写入文件，执行sql语句
def mysql(mysqltext):
    file=open("/opt/codingPack/mySql.sql",'a')
    file.write(mysqltext)
    file.close()

# mysql("select * from test01; \n")
# mysql("create table if not exists  test02  (aa varchar2(20),bb varchar2(200));\n insert into test02(aa,bb) values('100000','枸杞');\n")
# res = subprocess.call("su - gbasedbt -c dbaccess gbase01@gbaseserver /opt/codingPack/mySql.sql  ",shell=True )
