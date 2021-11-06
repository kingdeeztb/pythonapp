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

cv2.VideoWriter_fourcc('P','I','M','1') = MPEG-1 codec  --MPEG-1编码类型，文件扩展名.avi。随机访问，灵活的帧率、可变的图像尺寸
cv2.VideoWriter_fourcc('M','J','P','G') = motion-jpeg codec   --> mp4v
cv2.VideoWriter_fourcc('M', 'P', '4', '2') = MPEG-4.2 codec
cv2.VideoWriter_fourcc('D', 'I', 'V', '3') = MPEG-4.3 codec
cv2.VideoWriter_fourcc('D', 'I', 'V', 'X') = MPEG-4 codec     --> avi
cv2.VideoWriter_fourcc('U', '2', '6', '3') = H263 codec
cv2.VideoWriter_fourcc('I', '2', '6', '3') = H263I codec
cv2.VideoWriter_fourcc('F', 'L', 'V', '1') = FLV1 codec FLV是FLASH VIDEO的简称，FLV流媒体格式是一种新的视频格式。由于它形成的文件极小、加载速度极快，
CV_FOURCC('A', 'V', 'C', '1')  ---H264
cv2.VideoWriter_fourcc('T','H','E','O')---OGGVorbis音频压缩格式，有损压缩，类似于MP3等的音乐格式。，兼容性差，件扩展名.ogv。
cv2.VideoWriter_fourcc('I','4','2','0')---未压缩的YUV颜色编码，4:2:0色度子采样。兼容性好，但文件较大。文件扩展名.avi。
————————————————
版权声明：本文为CSDN博主「初雪日」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/TionSu/java/article/details/81356006

'''
'''
Python+百度云盘2113
Python库
使用的Python库：bypy,网址：https://github.com/houtianze/bypy
安装：python -m pip install bypy
支持52612.7和3.3+
本例以Python3.4为例。
安装完成4102之后，直接1653在系统命令行中输入bypy命令，将会列出所有的命令的使用信息。
授权
在命令行中输入bypy info，将会出现一个提示，按照提示完成授权，完成了授权Python代码才能和你的百度云盘进行通信。
常用命令
新建文件夹，在百度网盘中新建一个文件夹：
mkdir(remotepath='bypy')，将会新建一个bypy文件夹，如图：
新建的文件夹
上传文件：
upload(localpath='c:\\new\\timg.jpg',remotepath='bypy',ondup='newcopy')
参数说明：
localpath:本地的目录，如果省略则为当前目录。
remotepath:云盘目录
ondup:当出现重复文件时如何处理，默认是overwrite,安全起见可以更改为newcopy
Python 代码实例
from bypy import ByPy
bp = ByPy()
bp.mkdir(remotepath='bypy')
bp.upload(localpath='c:\\new\\timg.jpg',remotepath='bypy',ondup='newcopy')
print('上传完毕！')
注意：
中文文件名可能会出现问题,最好使用英文文件名。



1.下载cmake

pip install cmake
2.下载scikit-image

pip install scikit-image
3.下载dlib（现在的新版本不需要Boost）

pip install dlib
pip install face_recognition
'''

from cv2 import cv2
import time
#from bypy import ByPy


times_2 = time.strftime('%Y_%m_%d_%H_%M_%S',
                        time.localtime(time.time()))  # 本地保存的视频名称时间戳


def video_names(name, type):
    names = name+'_'+times_2+"."+type
    return names


def time_update():
    time.sleep(0)
    time_new = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time()))
    return(time_new)


def ip_cammer(video_full_path, video_formate, video_logo, video_exit, video_name):
    # video_full_path = "http://admin:admin@192.168.25.87:8081/video"
    video_url = video_full_path
    # 参数为0时调用本地摄像头；url连接调取网络摄像头；文件地址获取本地视频

    cap = cv2.VideoCapture(video_url)  # 网络摄像头

    fourcc = cv2.VideoWriter_fourcc(*video_formate)
    # fps = cap.get(cv2.CAP_PROP_FPS)
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    out = cv2.VideoWriter(str(video_name), fourcc, 25.0, size)

    # cv2.VideoWriter这个函数，需要参数有视频名, 格式, 码率(fps), 帧的尺寸等参数
    while True:
        try:
            ret, frame = cap.read()  # 网络摄像头
            out.write(frame)

            # 在图像上显示 Press Q to save and quit
            cv2.putText(frame, video_logo + ' '+time_update(), (10, 450),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

            # ret, frame_local = cap_local.read()#本地摄像头
            # 灰度化如果输出为灰度,请使用这个.
            #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # 横向翻转
            # frame_local = cv2.flip(frame_local, 1)

            # cv2.imshow('frame', gray)显示为灰度图片
            # 以下三行代码可以决定窗口是否显示,网络摄像头显示
            cv2.imshow('CamerShow', frame)  # 显示为正常图片 f
        except Exception as re:
            print("请检查网络摄像头连接是否正常.")
            break    
        if cv2.waitKey(1) & 0xFF == ord(video_exit):
            break
    cap.release()
    cv2.destroyAllWindows()

def local_cammer(video_formate, video_logo, video_exit, video_name):
    cap_local = cv2.VideoCapture(0)  # 本地摄像头
    fourcc = cv2.VideoWriter_fourcc(*video_formate)

    size = (int(cap_local.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(cap_local.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    out = cv2.VideoWriter(str(video_name), fourcc, 25.0, size)
    # cv2.VideoWriter这个函数，需要参数有视频名, 格式, 码率(fps), 帧的尺寸等参数

    # # 告诉OpenCV使用人脸识别分类器===
    # classfier = cv2.CascadeClassifier("C:\\Users\\w_zhangtb\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt.xml")
    # color = (0, 255, 0)
    # num = 0
    # # ===============是否需要人脸检测模块================#
    
    while True:
        ret, frame_local = cap_local.read()  # 本地摄像头

        # 灰度化如果输出为灰度,请使用这个.
        grey = cv2.cvtColor(frame_local, cv2.COLOR_BGR2GRAY)
        # 横向翻转
        # frame_local = cv2.flip(frame_local, 1)

        # # ===============是否需要人脸检测模块================#
        # # 人脸检测，1.2和2分别为图片缩放比例和需要检测的有效点数
        # faceRects = classfier.detectMultiScale(grey, scaleFactor=1.2, minNeighbors=3, minSize=(10, 10))

        # for faceRect in faceRects:
        #     #单独框出每一张人脸
        #     x, y, w, h = faceRect
        #     # img_name = "%s/%d.jpg" % ( "D:\\pythonApp\\image",10)

        #     # image = frame_local[y - 10: y + h + 10, x - 10: x + w + 10]
        #     # cv2.imwrite(img_name, image, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
        #     num += 1
        #     # 画出矩形框
        #     cv2.rectangle(frame_local, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)
        # # ===============是否需要人脸检测模块================#

        out.write(frame_local)
        # 在图像上显示 Press Q to save and quit
        cv2.putText(frame_local,
                    video_logo + ' '+time_update(),
                    (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (255, 255, 255), 2)

        # cv2.imshow('frame', gray)显示为灰度图片

        # 以下三行代码可以决定窗口是否显示,网络摄像头显示
        # 本地摄像头显示
        cv2.imshow('CamerShow_local', frame_local)  # 显示为正常图片

        if cv2.waitKey(1) & 0xFF == ord(video_exit):
            break
            key=cv2.waitKey(10)

    cap_local.release()
    cv2.destroyAllWindows()

#===============================================
# 摄像头调用===========
url = 'http://admin:admin@192.168.22.48:8081/video'
#视频流类型
types = 'FLV1'
#视频水印
logo = 'Press Q to exit'
#退出键
exit_button='q'
#视频名称
w = video_names("cammer", "flv")

ip_cammer(url, types, logo, exit_button, w)
# local_cammer(types, logo, exit_button, w)
#===============================================
