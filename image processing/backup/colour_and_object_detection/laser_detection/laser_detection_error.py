import cv2
import numpy as np
import colorsys
from numpy import interp
import time
cap=cv2.VideoCapture(0)

def movement():
	_,frame=cap.read()
	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	red_up=np.array([180,255,360])
	red_down=np.array([166,100,80])
	
	mask=cv2.inRange(hsv,red_down,red_up)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)
	res=cv2.bitwise_and(frame,frame,mask=mask)
	the=cv2.adaptiveThreshold(mask,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,5)
	contours,hierarchy = cv2.findContours(the, 1, 2)
	cnt = contours[0]
	(x,y),radius = cv2.minEnclosingCircle(cnt)
	center = (int(x),int(y))
	
	radius = int(radius)
	for xa in range (radius*2):
		for ya in range(radius*2):
			d=abs(((x-x-radius+xa)**2)+((y-y-radius+ya)**2))**0.5
			d=int(d)
			if(d>=radius):
				a=frame[xa+x-radius,ya+y-radius]
				a=[180,255,255]
				frame[xa+x-radius,ya+y-radius]=a
	
	img = cv2.circle(frame,center,radius,(255,0,0),2)
	print radius,d
	cv2.imshow('frame2',frame)
	cv2.waitKey(2)

	
		
		
while(1):
	
	movement()
	
