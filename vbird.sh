#!/bin/bash
# Program:
# Using netstat and grep to detect WWW,SSH,FTP and Mail services.
# History:
# 2015/07/16 VBird First release
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH
ipaddress=/home/tianbo/netstat_checking.txt
netstat -tuln >${ipaddress}
print_ipadd=$(grep ":50370" ${ipaddress})

if [ "${print_ipadd}" != "" ]; then
    echo "${print_ipadd}"
elif [ "${print_ipadd}" == "" ]; then
    echo "啥都没有啊？"
else
    echo "你输入的是啥？"
fi
