#laser detection

import cv2
import numpy as np
import colorsys
from numpy import interp
import time

cap=cv2.VideoCapture(0)
while(1):
	_,frame=cap.read()
	frame = frame[220:260,1:640]
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	pink_up=np.array([165,255,255])
	pink_down=np.array([144,30,150])

	red_up=np.array([180,255,360])
	red_down=np.array([166,100,80])
	
	laser_up=np.array([30,30,150])
	laser_down=np.array([0,20,140])

	white_up=np.array([180,10,240])
	white_down=np.array([0,0,230])

	mask=cv2.inRange(gray,225,227)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)
	res=cv2.bitwise_and(frame,frame,mask=mask)
	the=cv2.adaptiveThreshold(mask,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,5)
	contours,hierarchy = cv2.findContours(the,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cnt = contours[0]
	print contours
	(x,y),radius = cv2.minEnclosingCircle(cnt)
	center = (int(x),int(y))
	radius = int(radius)
	img = cv2.circle(frame,center,radius,(255,255,255),2)

			
	mask1=cv2.inRange(hsv,red_down,red_up)
	mask1= cv2.erode(mask1, None, iterations=2)
	mask1= cv2.dilate(mask1, None, iterations=2)
	res1=cv2.bitwise_and(frame,frame,mask=mask1)
	the1=cv2.adaptiveThreshold(mask1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,5)
	contours1,hierarchy1 = cv2.findContours(the1, 1, 2)
	cnt1 = contours1[0]
	(x1,y1),radius1 = cv2.minEnclosingCircle(cnt1)
	center1 = (int(x1),int(y1))
	radius1= int(radius1)
	img1 = cv2.circle(frame,center1,radius1,(255,0,0),2)

	if (x1>0 and x>0):
		xd=(center[0]-center1[0])
		yd=(center[1]-center1[1])
		d=int(((xd**2)+(yd**2))**0.5)
	
	print d
	cv2.imshow('frame',frame)
	cv2.imshow('blur',res1)
	cv2.imshow('blur1',res)
	cv2.waitKey(1)
