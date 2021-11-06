'''
#!/usr/bin/env python

# coding:utf-8

import numpy as np
import cv2

capture = cv2.VideoCapture(0)#参数为0时调用本地摄像头；url连接调取网络摄像头；文件地址获取本地视频
while True:
    ret, frame = capture.read()
    #灰度化
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #普通图片
    cv2.imshow('CamerShow', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()

# 导入time模块
import time
# 优化格式化化版本
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))


5、time.strftime的参数
strftime(format[, tuple]) -> string
将指定的struct_time(默认为当前时间)，根据指定的格式化字符串输出
python中时间日期格式化符号：
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12） 
%M 分钟数（00=59）
%S 秒（00-59）

%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
#-------------------------------------------生成exe文件----------
# upload("host.txt")
# pip install pywin32 #生成exe文件
# "pyinstaller -F d:\\pythonApp\\cammer.py --noconsole"           #生成exe文件

# 从python对应的路径中拷贝 opencv_video_ffmpeg412_64.dll 到exe旁边。可能不同的python和opencv版本对应的文件名和数字不一样，大家自己测试以下即可。

# 我用的Anaconda来管理python环境，因此我从 Anaconda3\\envs\\（环境名） 下将所有包含ffmpeg的dll文件都拷贝过去了，然后发现是 opencv_video_ffmpeg412_64.dll 的问题。
# "C:\\Users\\w_zhangtb\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\cv2\\opencv_videoio_ffmpeg420_64.dll"
#-------------------------------------------生成exe文件----------

Python 上传文件到百度网盘
关于如何获取 access_token 这个可以自己查百度开放的OAuth 2.0 的 API。这里不做介绍。

第三方 Python 库
poster

# coding:UTF-8
import urllib
import urllib2

__author__ = 'Administrator'
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

register_openers()

def upload(fileName):
    """
    通过百度开发者 API 上传文件到百度云
    """
    datagen, headers = multipart_encode({"file": open("E:\\PHPTest\\Test1\\%s"%fileName, "rb")})
    baseurl = "https://pcs.baidu.com/rest/2.0/pcs/file?"
    args = {
        "method": "upload",
        "access_token": "0.a2834e35964a7b0704242wef160507c1.2592000.1386326697.1060338330-1668780",
        "path": "/apps/ResourceSharing/%s"%fileName
    }
    encodeargs = urllib.urlencode(args)
    url = baseurl + encodeargs

    print(url)

    request = urllib2.Request(url, datagen, headers)
    result = urllib2.urlopen(request).read()
    print(result)

    cv2.putText(img, str(i), (123,456)), font, 2, (0,255,0), 3) 
    各参数依次是：图片，添加的文字，左上角坐标，字体，字体大小，颜色，字体粗细其中字体可以选择 
    字体大小，数值越大，字体越大字体粗细，越大越粗，数值表示描绘的线条占有的直径像素个数
    Python:img =cv.putText(img, text, org, fontFace,fontScale,color[, thickness[, lineType[, bottomLeftOrigin]]])

'''


from cv2 import cv2
import time


def time_update():
    time.sleep(0)
    time_new = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time()))
    return(time_new)


times = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 时间戳
times_2 = time.strftime('%Y_%m_%d_%H_%M_%S',
                        time.localtime(time.time()))  # 时间戳
video_name = 'camer_'+times_2+'.avi'

print(video_name)
# video_full_path = "http://admin:admin@192.168.22.45:8081/video"
# cap = cv2.VideoCapture(video_full_path)
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# fps = cap.get(cv2.CAP_PROP_FPS)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
out = cv2.VideoWriter(str(video_name), fourcc, 10.0, size)
# cv2.VideoWriter这个函数，需要参数有视频名, 格式, 码率(fps), 帧的尺寸等参数

while True:
    ret, frame = cap.read()
    # 灰度化如果输出为灰度,请使用这个.
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 横向翻转
    #frame = cv2.flip(frame, 1)
    out.write(frame)
    # 在图像上显示 Press Q to save and quit
    cv2.putText(frame,
                "Press Q to Save&Quit"+' '+time_update(),
                (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (255,255,255), 2)
    # cv2.imshow('frame', gray)显示为灰度图片
    # 以下三行代码可以决定窗口是否显示.
    cv2.imshow('CamerShow', frame)  # 显示为正常图片
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
