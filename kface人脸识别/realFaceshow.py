from cv2 import cv2

import numpy as np

cv2.namedWindow("faceCatch")

cap=cv2.VideoCapture(0) 
# cap=cv2.VideoCapture("http://admin:admin@192.168.25.62:8081/video") 


success, frame = cap.read()

color = (0,255,0)

classfier=cv2.CascadeClassifier("C:\\Users\\w_zhangtb\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt.xml")

while success:

    success, frame = cap.read()

    size=frame.shape[:2]

    image=np.zeros(size,dtype=np.float16)

    frame = cv2.flip(frame, 1)

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.equalizeHist(image, image)

    divisor=8

    h, w = size

    minSize =(w//divisor, h//divisor)   

    faceRects = classfier.detectMultiScale(image, 1.2, 2, cv2.CASCADE_SCALE_IMAGE,minSize)

    if len(faceRects)>0:

        for faceRect in faceRects: 

                x, y, w, h = faceRect
                cv2.rectangle(frame, (x, y), (x+w, y+h), color)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, "FaceShowing...",(x + 40, y + 40), font, 0.7, (255,0,255),2)

    cv2.imshow("faceCatch", frame)

    key=cv2.waitKey(10)

    c = chr(key & 255)

    if c in ['q', 'Q', chr(27)]:

        break

cv2.destroyWindow("faceCatch")