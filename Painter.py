import os
import time
import numpy as np
import cv2
import pyautogui
import Hand_Tracking
detector=Hand_Tracking.Hand_Tracker()
brushthickness=5
eraserthickness=25
cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
color=(0,255,0)
xp,yp=0,0
path="Resources"
listdir=os.listdir(path)
overlay=[]
img_canvas=np.zeros((720,1280,3),np.uint8)
for i in listdir:
    img=cv2.imread(path+"/"+i)
    overlay.append(img)
header=overlay[0]
while True:
    #Import the image
    success,img=cap.read()
    img=cv2.flip(img,1)
    img[0:125,0:1280]=header
    #Finding landmarks
    detector.draw_Hands(img)
    landmarks=detector.Find_Landmarks(img,draw=False)
    #Fingers up
    if len(landmarks)!=0:
        fingers=detector.Fingers_up()
        #print(fingers)
        x1,y1=landmarks[8][1:]
        x2,y2=landmarks[12][1:]
        #Selection Mode
        if fingers[1]==1 and fingers[2]==1:
            xp, yp = 0, 0
            if y1<125:
                if 270<x1<470:
                    header=overlay[2]
                    color=(0,0,255)
                elif 500<x1<770:
                    header=overlay[1]
                    color=(255,0,0)
                elif 800<x1<1050:
                    header=overlay[0]
                    color=(0,255,0)
                elif 1050<x1<1250:
                    header=overlay[3]
                    color=(0,0,0)
            cv2.rectangle(img, (x1, y1-30), (x2, y2+30), color,cv2.FILLED)
        #Drawing mode
        if fingers[1]==1 and fingers[2]==0:
            cv2.circle(img,(x1,y1),10,color,cv2.FILLED)
            if xp==0 and yp==0:
                xp,yp=x1,y1
            if color==(0,0,0):
                cv2.line(img,(xp,yp),(x1,y1),color,eraserthickness)
                cv2.line(img_canvas, (xp, yp), (x1, y1), color, eraserthickness)
            else:
                cv2.line(img, (xp, yp), (x1, y1), color, brushthickness)
                cv2.line(img_canvas, (xp, yp), (x1, y1), color, brushthickness)
            xp,yp=x1,y1
    img_gray=cv2.cvtColor(img_canvas,cv2.COLOR_BGR2GRAY)
    _,inv_image=cv2.threshold(img_gray,50,255,cv2.THRESH_BINARY_INV)
    inv_image=cv2.cvtColor(inv_image,cv2.COLOR_GRAY2BGR)
    img=cv2.bitwise_and(img,inv_image)
    img=cv2.bitwise_or(img,img_canvas)
    cv2.imshow("img", img)
    if cv2.waitKey(1) and 0XFF==ord('p'):
        break
