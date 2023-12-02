import cv2
import Hand_Tracking
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
detector=Hand_Tracking.Hand_Tracker()

while True:
    success,img=cap.read()
    detector.draw_Hands(img)
    landmarks=detector.Find_Landmarks(img,draw=False)
    if len(landmarks)!=0:
        points,length=detector.find_length(img,landmarks[8][0],landmarks[12][0])
    fingers=detector.Fingers_up()
    print(fingers)
    cv2.imshow("img",img)
    if cv2.waitKey(1) and 0XFF==ord('p'):
        break