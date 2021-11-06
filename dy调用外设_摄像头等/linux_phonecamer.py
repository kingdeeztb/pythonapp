
#!/usr/bin/env python

# coding:utf-8



from cv2 import cv2
import time
from bypy import ByPy

bp=ByPy()



times_2 = time.strftime('%Y_%m_%d_%H_%M_%S',
                        time.localtime(time.time()))  


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
    

    cap = cv2.VideoCapture(video_url) 

    fourcc = cv2.VideoWriter_fourcc(*video_formate)
    # fps = cap.get(cv2.CAP_PROP_FPS)
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    out = cv2.VideoWriter(str(video_name), fourcc, 25.0, size)

    
    while True:
        try:
            ret, frame = cap.read() 
            out.write(frame)

           
            cv2.putText(frame, video_logo + ' '+time_update(), (10, 450),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

           
            cv2.imshow('CamerShow', frame) 
        except Exception as re:

            break    
        if cv2.waitKey(1) & 0xFF == ord(video_exit):
            break
    cap.release()
    cv2.destroyAllWindows()

def local_cammer(video_formate, video_logo, video_exit, video_name):
    cap_local = cv2.VideoCapture(0) 
    fourcc = cv2.VideoWriter_fourcc(*video_formate)

    size = (int(cap_local.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(cap_local.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    out = cv2.VideoWriter(str(video_name), fourcc, 25.0, size)
   
    
    while True:
        ret, frame_local = cap_local.read() 

       
        grey = cv2.cvtColor(frame_local, cv2.COLOR_BGR2GRAY)
        

        out.write(frame_local)
       
        cv2.putText(frame_local,
                    video_logo + ' '+time_update(),
                    (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (255, 255, 255), 2)

       
        cv2.imshow('CamerShow_local', frame_local) 

        if cv2.waitKey(1) & 0xFF == ord(video_exit):
            break
            key=cv2.waitKey(10)

    cap_local.release()
    cv2.destroyAllWindows()

url = 'http://admin:admin@192.168.43.1:8081/video'

types = 'FLV1'

logo = 'Press Q to exit'

exit_button='q'

w = video_names("cammer", "flv")

ip_cammer(url, types, logo, exit_button, w)
#local_cammer(types, logo, exit_button, w)
bp.mkdir(remotepath='Python_avi')
bp.upload(localpath='/home/tianbo/pythonApp',remotepath='Python_avi',ondup='overwiter')
bp.info()
