import cv2
import time

def time_update():
    time.sleep(0)
    time_new = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time()))
    return(time_new)

times_2 = time.strftime('%Y_%m_%d_%H_%M_%S',
                        time.localtime(time.time()))  # 本地保存的视频名称时间戳
video_name = 'camer_'+times_2+'.flv'
print(video_name)

video_full_path = "http://admin:admin@192.168.22.45:8081/video"
#参数为0时调用本地摄像头；url连接调取网络摄像头；文件地址获取本地视频
cap = cv2.VideoCapture(video_full_path)#网络摄像头
# cap_local = cv2.VideoCapture(0)#本地摄像头


fourcc = cv2.VideoWriter_fourcc(*'FLV1')
# fps = cap.get(cv2.CAP_PROP_FPS)

size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
out = cv2.VideoWriter(str(video_name), fourcc, 25.0, size)
# cv2.VideoWriter这个函数，需要参数有视频名, 格式, 码率(fps), 帧的尺寸等参数

while True:
    ret, frame = cap.read()#网络摄像头
    # ret, frame_local = cap_local.read()#本地摄像头
    # 灰度化如果输出为灰度,请使用这个.
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 横向翻转
    # frame_local = cv2.flip(frame_local, 1)
    out.write(frame)
    # 在图像上显示 Press Q to save and quit
    cv2.putText(frame,
                "Press Q to Save&Quit"+' '+time_update(),
                (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (255, 255, 255), 2)
    # cv2.imshow('frame', gray)显示为灰度图片
    # 以下三行代码可以决定窗口是否显示,网络摄像头显示
    cv2.imshow('CamerShow', frame)  # 显示为正常图片 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #本地摄像头显示
    # cv2.imshow('CamerShow_local', frame_local)  # 显示为正常图片
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break    
cap.release()