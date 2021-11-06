# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#设置工作路径
import os
os.chdir('E:\\0yfl\\SH-spyder-workspace\\')
os.path.abspath('.')


import numpy as np
import cv2

#1.1读取图片imread；展示图片imshow；导出图片imwrite
#只是灰度图片
img=cv2.imread('Myhero.jpg',cv2.IMREAD_GRAYSCALE)
#彩色图片
img=cv2.imread('Myhero.jpg',cv2.IMREAD_COLOR)
#彩色以及带有透明度
img=cv2.imread('Myhero.jpg',cv2.IMREAD_UNCHANGED)
print(img)
#设置窗口可自动调节大小
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
k=cv2.waitKey(0)
#如果输入esc
if k==27:
    #exit
    cv2.destroyAllWindows
#如果输入s
elif k==ord('s'):
    #save picture and exit
    cv2.imwrite('Myhero_out.png',img)
    cv2.destroyAllWindows()


#1.2视频读取
#打开内置摄像头
cap=cv2.VideoCapture(0)
#打开视频
cap=cv2.VideoCapture('why.mp4')
#或者视频每秒多少帧的数据
fps=cap.get(5)
i=0
while(True):
    #读取一帧
    ret,frame=cap.read()
    #转化为灰图
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #设置导出文件名编号
    i = i + 1
    #每1s导出一张
    if i/fps==int(i/fps):
        #导出文件名为why+编号+.png
        #若想要导出灰图，则将下面frame改为gray即可
        cv2.imwrite("why"+str(int(i/fps))+".png",frame)
    #读完之后结束退出
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destoryAllWindows()


#1.3图像像素修改
rangexmin=100
rangexmax=120
rangeymin=90
rangeymax=100
img=cv2.imread('Myhero.jpg',0)
img[rangexmin:rangexmax,rangeymin:rangeymax]=[[255]*(rangeymax-rangeymin)]*(rangexmax-rangexmin)
cv2.imwrite('Myhero_out2.png',img)

#拆分以及合并图像通道1
b,g,r=cv2.split(img)
img=cv2.merge(b,g,r)

#png转eps，不过非常模糊
from matplotlib import pyplot as plt
img=cv2.imread('wechat1.png',cv2.IMREAD_COLOR)
plt.imsave('wechat_out.eps',img)

#图像按比例混合
img1=cv2.imread('Myhero.jpg',cv2.IMREAD_COLOR)
img2=cv2.imread('Myhero_out.png',cv2.IMREAD_COLOR)
dst=cv2.addWeighted(img1,0.5,img2,0.5,0)
cv2.imwrite("Myhero_combi.jpg",dst)


#1.4按位运算
#加载图像
img1=cv2.imread("Myhero.jpg")
img2=cv2.imread("why1.png")
#后面那张图更大
rows,cols,channels=img1.shape
ROI=img2[0:rows,0:cols]
#做一个ROI为图像的大小
img2gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
#小于175的改为0，大于175的赋值为255
ret,mask=cv2.threshold(img2gray,175,255,cv2.THRESH_BINARY)
cv2.imwrite("Myhero_mask.jpg",mask)
#255-mask=mask_inv
mask_inv=cv2.bitwise_not(mask)
cv2.imwrite("Myhero_mask_inv.jpg",mask_inv)
#在mask白色区域显示成ROI，背景图片
img2_bg=cv2.bitwise_and(ROI,ROI,mask=mask)
cv2.imwrite("Myhero_pic2_backgroud.jpg",img2_bg)
#除了mask以外的区域都显示成img1，前景图片
img1_fg=cv2.bitwise_and(img1,img1,mask=mask_inv)
cv2.imwrite("Myhero_pic2_frontgroud.jpg",img1_fg)
#前景图片加上背景图片
dst = cv2.add(img2_bg,img1_fg)
img2[0:rows, 0:cols ] = dst
cv2.imwrite("Myhero_pic2_addgroud.jpg",dst)
#finished

#构建淹膜方法2
#截取帧
ret,frame=cap.read()
#转换到HSV
hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#设定蓝色的阈值
lower_blue=np.array([110,50,50])
upper_blue=np.array([130,255,255])
#根据阈值构建掩模
mask=cv2.inRange(hsv,lower_blue,upper_blue)
#对原图像和掩模进行位运算
res=cv2.bitwise_and(frame,frame,mask=mask)


#图片放缩，用的插值方法，所以不会损害清晰度
res=cv2.resize(img1,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
cv2.imwrite("Myhero_bigger.jpg",res)
#第二种插值方法
height,width=img.shape[:2]
res=cv2.resize(img,(2*width,2*height),interpolation=cv2.INTER_CUBIC)

#edge现实图片中不好用，人工画的图片还可以
img = cv2.imread('why3.png',0)
edges = cv2.Canny(img,50,100)
cv2.imwrite("why3_edge.png",edges)

#识别轮廓，并保存轮廓点contours
img=cv2.imread('why129.png')
imgray=cv2.imread('why129.png',cv2.IMREAD_GRAYSCALE)
ret,thresh = cv2.threshold(imgray,127,255,0)
cv2.imwrite("2.jpg",thresh)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img = cv2.drawContours(img, contours, -1, (0,255,0), 3)
cv2.imwrite("3.jpg",img)


#轮廓
img = cv2.imread('why3.png',0)
ret,thresh = cv2.threshold(img,127,255,0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0] 
#近似轮廓
epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)

img = cv2.drawContours(img, approx, -1, (0,255,0), 3)
cv2.imwrite("4.jpg",img)

from matplotlib import pyplot as plt
#图像识别/匹配
img_rgb = cv2.imread('why174.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
img2=img_gray.copy()
template = cv2.imread('0temp.png',0)
w, h = template.shape[::-1]
#共有六种识别方法
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    #eval返回某个式子的计算结果
    method = eval(meth)
    #下面使用匹配方法
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    #画矩形把他框出来
    cv2.rectangle(img,top_left, bottom_right, 255, 2)
    
    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    
    plt.show()
    
#这个匹配结果太差
#选取3，5，6的匹配方式会稍微好点：cv2.TM_CCORR；cv2.TM_SQDIFF，cv2.TM_SQDIFF_NORMED

#视频人脸识别
#https://blog.csdn.net/wsywb111/article/details/79152425
import cv2
from PIL import Image
cap=cv2.VideoCapture("why.mp4")
#告诉Opencv使用人脸识别分类器
classfier=cv2.CascadeClassifier("E:\\0yfl\\opencv-master\\data\\haarcascades\\haarcascade_frontalface_alt2.xml")
count=0
while cap.isOpened():
    ret,frame=cap.read()
    if not ret:
        break
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faceRect=classfier.detectMultiScale(grey,scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
    if len(faceRect)>0:
        count=count+1
print(count)


#137这种程度可以识别，111没有成功识别，大概是侧脸的缘故
#截出人脸
image_name="why111.png"
frame=cv2.imread(image_name,0)
if not (frame is None):
    #导入测试集
    classfier=cv2.CascadeClassifier("E:\\0yfl\\opencv-master\\data\\haarcascades\\haarcascade_frontalface_alt2.xml")
    #使用测试集导出人脸的位置，存在faceRect中，可以检测多张人脸
    faceRect=classfier.detectMultiScale(frame,scaleFactor=3.0, minNeighbors=3, minSize=(32, 32))
    count=0
    for (x1,y1,w,h) in faceRect:
        count=count+1
        #截取上述图片的人脸部分并保存每一张识别出的人脸
        Image.open(image_name).crop((x1,y1,x1+w,y1+h)).save(image_name.split(".")[0]+"_face_"+str(count)+".png")
    if count==0:
        print ("No face detected!")
else:
    print ("Picture "+ image_name +" is not exist in "+os.path.abspath("."))
#人脸上画出矩形
from PIL import Image,ImageDraw
image_name="why111.png"
frame=cv2.imread(image_name,0)
if not (frame is None):
    classfier=cv2.CascadeClassifier("E:\\0yfl\\opencv-master\\data\\haarcascades\\haarcascade_frontalface_alt2.xml")
    faceRect=classfier.detectMultiScale(frame,scaleFactor=3.0, minNeighbors=3, minSize=(32, 32))
    #画框框
    img = Image.open(image_name)
    draw_instance = ImageDraw.Draw(img)
    count=0
    for (x1,y1,w,h) in faceRect:
        draw_instance.rectangle((x1,y1,x1+w,y1+h), outline=(255, 0,0))
        img.save('drawfaces_'+image_name)
        count=count+1
    if count==0:
        print ("No face detected!")
else:
    print ("Picture "+ image_name +" is not exist in "+os.path.abspath("."))


#detectFaces()返回图像中所有人脸的矩形坐标（矩形左上、右下顶点）
#使用haar特征的级联分类器haarcascade_frontalface_default.xml，在haarcascades目录下还有其他的训练好的xml文件可供选择。
#注：haarcascades目录下训练好的分类器必须以灰度图作为输入。


from PIL import Image,ImageDraw
image_name="why63.png"
frame=cv2.imread(image_name,0)
if not (frame is None):
    classfier=cv2.CascadeClassifier("E:\\0yfl\\opencv-master\\data\\haarcascades\\haarcascade_fullbody.xml")
    faceRect=classfier.detectMultiScale(frame,scaleFactor=3.0, minNeighbors=3, minSize=(32, 32))
    #画框框
    img = Image.open(image_name)
    draw_instance = ImageDraw.Draw(img)
    count=0
    for (x1,y1,w,h) in faceRect:
        draw_instance.rectangle((x1,y1,x1+w,y1+h), outline=(255, 0,0))
        img.save('drawfaces_'+image_name)
        count=count+1
    if count==0:
        print ("No face detected!")
else:
    print ("Picture "+ image_name +" is not exist in "+os.path.abspath("."))