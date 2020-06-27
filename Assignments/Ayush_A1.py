# import necessary modules
import imutils
import cv2
import numpy as np
from imutils.video import VideoStream
import time
import argparse
from collections import deque


# take in arguements from command line
ap = argparse.ArgumentParser()
ap.add_argument("-v","--video",required=False,help="path to video")
ap.add_argument("-b","--buffer",required=False,type = int,help="size of tracking coordinates' deque")
arguements = vars(ap.parse_args())

# start video and allow warmup
print("Starting the video..")
video = cv2.VideoCapture(arguements["video"])
time.sleep(2.0)


lowerColorBound = (24,102,77)
upperColorBOund = (64, 255, 255)
tracking_coordinates = deque(maxlen=arguements["buffer"])

# take frame from video
while True:
	# read each frame in variable "frame" and resize it
	frame = video.read()
	if frame is None:
		break

	# blur(to reove noise),convert to grey,find edges in frame
	blur = cv2.GaussianBlur(frame,(11,11),0)
	edges = cv2.Canny(blur,20,70)
	hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, lowerColorBound, upperColorBOund)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)

	# find contours in frame
	cnts = cv2.findContours(mask.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	cnts2 = cv2.findContours(edges.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	cnts2 = imutils.grab_contours(cnts)
	center = None
	ballCnt = None
	
	# model via color detection
	if len(cnts)>0:
		ballCnt = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(ballCnt)

		# M = cv2.moments(ballCnt[0])
		center = (int(x),int(y))

		#draw the ball contour and update tracking coordinates
		if radius > 10:
			cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
			cv2.circle(frame, center, 3, (0, 0, 255), -1)


	# model via edge recognition
	# iterating the contours
	# for c in cnts2:
	# 	# approximate the contour
	# 	peri = cv2.arcLength(c, True)
	# 	approx = cv2.approxPolyDP(c, 0.02 * peri, True)


	# 	# if our approximated contour has zero points, then we can assume that we have found our ball
	# 	if len(approx) == 0:
	# 		ballCnt = approx
	# 		break

	# find out the radius and center of the ball contour
	

	tracking_coordinates.append(center)

	# # draw trail
	for i in range(1,len(tracking_coordinates)):
		if tracking_coordinates[i - 1] is None or tracking_coordinates[i] is None:
			continue

		cv2.line(frame,tracking_coordinates[i-1],tracking_coordinates[i],(255,0,0),1)

	# show the frame 
	cv2.imshow("Frame", frame)

	# stop code on pressing "q"
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break

cv2.destroyAllWindows()



