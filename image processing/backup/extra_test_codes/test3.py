import cv2
import numpy as np
import colorsys
x=0
y=0
cap=cv2.VideoCapture(0)
#f= open("testdata.txt","w+")
while(1):
	_,frame=cap.read()
	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	pink_up=np.array([165,255,255])
	pink_down=np.array([144,30,150])
	#red_up=np.array([228,229,232])
	#red_down=np.array([224,225,228])
	white_up=np.array([180,10,240])
	white_down=np.array([0,0,230])
	mask1=cv2.inRange(hsv,white_down,white_up)
	mask1= cv2.erode(mask1, None, iterations=2)
	mask1= cv2.dilate(mask1, None, iterations=2)
	res1=cv2.bitwise_and(frame,frame,mask=mask1)
	the1=cv2.adaptiveThreshold(mask1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,5)
	#cnts1, _ = cv2.findContours(image.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2:]
	
	contours1,hierarchy1 = cv2.findContours(the1, 1, 2)
	cnt1 = contours1[0]
	(x1,y1),radius1 = cv2.minEnclosingCircle(cnt1)
	center1 = (int(x1),int(y1))
	radius1= int(radius1)
	img1 = cv2.circle(frame,center1,radius1,(0,0,255),2)

	mask=cv2.inRange(hsv,pink_down,pink_up)
	mask= cv2.erode(mask, None, iterations=2)
	mask= cv2.dilate(mask, None, iterations=2)
	res=cv2.bitwise_and(frame,frame,mask=mask)
	the=cv2.adaptiveThreshold(mask,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,5)
	#cnts, _ = cv2.findContours(image.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2:]
	contours,hierarchy = cv2.findContours(the, 1, 2)
	cnt = contours[0]
	(x,y),radius = cv2.minEnclosingCircle(cnt)
	center = (int(x),int(y))
	radius= int(radius)
	img = cv2.circle(frame,center,radius,(0,0,255),2)
	xd=abs(center[0]-center1[0])
	yd=abs(center[1]-center1[1])
	d=pow((pow(xd,2)+pow(yd,2),0.5)
	
	print d
	
	cv2.imshow('frame',frame)
	cv2.imshow('blur',res1)
	
	cv2.waitKey(1)
