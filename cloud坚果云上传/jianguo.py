from webdav3.client import Client
from datetime import datetime
from webdav3.exceptions import LocalResourceNotFound

import math
# invoke this function every day.
def upload():
    options = {
        #'webdav_hostname': "网盘地址，如果是坚果云，不能只输入/dav/路径，似乎这个文件夹不能访问，在下面再建一个文件夹，比如backup。网址中需要有backup的地址比如https://dav.jianguoyun.com/dav/backup",
        'webdav_hostname':"https://dav.jianguoyun.com/dav/python_avi",
        'webdav_login': "***********",
        'webdav_password': "ahq8t4xp73nswrdz***",
        'disable_check': True, #有的网盘不支持check功能
    }
    client = Client(options)
        # 我选择用时间戳为备份文件命名
    #file_name = str(math.floor(datetime.now().timestamp())) + '.bak'
    file_name=r'/a.txt'#绝对地址
    try:
        # 写死的路径，第一个参数是网盘地址
        client.upload(file_name,r'/a.txt')
        # 打印结果，之后会重定向到log
        print('upload at ' + file_name)
    except LocalResourceNotFound as exception:
        print('An error happen: LocalResourceNotFound ---'  + file_name)
# 如果是直接调用文件，执行upload()if __name__ == '__main__':
    print('run upload')
upload()
