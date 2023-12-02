import cv2
import mediapipe as mp
import math
class Hand_Tracker():
    def __init__(self,mode=False,Tracking_con=0.5,Detection_con=0.5,max_hands=1):
        self.mode=mode
        self.Detection_con=Detection_con
        self.Tracking_con=Tracking_con
        self.max_hands=max_hands
        self.mp_hands=mp.solutions.hands
        self.Hands=self.mp_hands.Hands(max_num_hands=1)
        self.draw=mp.solutions.drawing_utils
    def draw_Hands(self,img,draw=True):
        img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.result=self.Hands.process(img_rgb)
        if self.result.multi_hand_landmarks:
            for lms in self.result.multi_hand_landmarks:
                if draw:
                    self.draw.draw_landmarks(img,lms,self.mp_hands.HAND_CONNECTIONS)
    def Find_Landmarks(self,img,draw=True,Hand_no=0):
        self.landmark=[]
        x=[]
        y=[]
        box=[]
        h, w, c = img.shape
        if self.result.multi_hand_landmarks:
            hand_result=self.result.multi_hand_landmarks[Hand_no]
            for id,lms in enumerate(hand_result.landmark):
                cx,cy=int(lms.x*w),int(lms.y*h)
                x.append(cx)
                y.append(cy)
                self.landmark.append([id,cx,cy])
                if draw:
                    cv2.circle(img,(cx,cy),15,(255,0,0),cv2.FILLED)
            xmin,ymin=min(x),min(y)
            xmax,ymax=max(x),max(y)
            box.append([xmin-20,ymin-20])
            box.append([xmax+20,ymax+20])
            cv2.rectangle(img,box[0],box[1],[0,255,0],2)
        return self.landmark
    def Fingers_up(self):
        tips=[4,8,12,16,20]
        up=[]
        #thumb
        if len(self.landmark)!=0:
            if self.landmark[tips[0]][1]>self.landmark[tips[0]-1][1]:
                up.append(1)
            else:
                up.append(0)
            for i in range(1,5):
                if self.landmark[tips[i]][2] < self.landmark[tips[i] - 2][2]:
                    up.append(1)
                else:
                    up.append(0)
        return up
    def find_length(self,img,p1,p2):
        x1,y1=self.landmark[p1][1:]
        x2,y2=self.landmark[p2][1:]
        cx=(x1-x2)//2
        cy=(y1-y2)//2
        cv2.line(img,(x1,y1),(x2,y2),(0,0,0),2)
        cv2.circle(img,(x1,y1),10,(255,255,0),cv2.FILLED)
        cv2.circle(img, (x2, y2), 10,(255,255,0), cv2.FILLED)
        cv2.circle(img, (x2+cx, y2+cy), 10,(255,0,255), cv2.FILLED)
        length=math.hypot(x1-x2,y1-y2)
        return [x1,x2,y1,y2,cx,cy],length

