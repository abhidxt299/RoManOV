import numpy as np
import time
import cv2
import imutils
import argparse
from collections import deque


ap=argparse.ArgumentParser()
ap.add_argument("-m","--max",type=int,default=64,help="maximum size")    #Added argument for maximum size of center track
args=vars(ap.parse_args())

hsv_red=cv2.cvtColor(np.uint8([[[0,0,255]]]),cv2.COLOR_BGR2HSV)
lower_bound=np.array([hsv_red[0][0][0]-10,100,100])           #These are lower and upper bound for a particular ball color.
upper_bound=np.array([hsv_red[0][0][0]+10,255,255])
center_track=deque(maxlen=args["max"])


cap=cv2.VideoCapture(0)                             #Starting VideoCapturing
while True:
    ret,frame=cap.read()
    if frame is None:
        break
    frame=imutils.resize(frame,width=400)           #Reduced frame size for increasing FPS
    blur_img=cv2.GaussianBlur(frame,(5,5),0)        #Used for reducing background noise
    hsv=cv2.cvtColor(blur_img,cv2.COLOR_BGR2HSV)    #Converted frame into hsv form

    mask=cv2.inRange(hsv,lower_bound,upper_bound)   #Mask is constructed for identifying red object.
    mask=cv2.erode(mask,None,iterations=4)          #Removes pixels from image esp. Noisy pixels.
    mask=cv2.dilate(mask,None,iterations=4)         #Add pixels to image boundaries,reducing background noises.



    cnts=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)        #Finding Contours.
    cnts=imutils.grab_contours(cnts)
    center=None

    if len(cnts)>0:
        c=max(cnts,key=cv2.contourArea)         #Identifying Biggest Contour.
        ((x,y),r)=cv2.minEnclosingCircle(c)
        M=cv2.moments(c)
        center=(int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))      #Centroid co-ordinates.

        if r > 5:
            cv2.circle(frame,(int(x),int(y)),int(r),(0,255,0),3)
    center_track.appendleft(center)

#In case if we need to detect the co-ordinates of center of the ball then the below code can be activated.
    # for i in range (1,len(center_track)):                               #For Tracking the co-ordinates of center.
    #     if center_track[i-1] is None or center_track[i] is None:
    #         continue
    #     cv2.line(frame,center_track[i-1],center_track[i],(255,0,0),2)
    cv2.imshow("Frame",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):                               #If q is pressed, Video is stopped.
        break
cap.release()
cv2.destroyAllWindows()
