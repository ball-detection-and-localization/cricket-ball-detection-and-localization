import cv2
import numpy as np
import colorsys
import time
count=0
rate=0
a=[]
b=[]
c=0
cap = cv2.VideoCapture('ball.webm')
while(rate<415):
	ret, frame = cap.read()
	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	#red_up=np.array([180,255,360])
	#red_down=np.array([166,100,80])
	
	red_up=np.array([175,255,255])
	red_down=np.array([165,100,100])
	cv2.line(frame,(0,480),(220,370),(0,255,0),2)
	cv2.line(frame,(640,480),(420,370),(0,255,0),2)
	cv2.line(frame,(220,370),(420,370),(0,255,0),2)
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
	img = cv2.circle(frame,center,radius,(255,0,0),2)
	if (center[0]>220 and center[0]<420 and center[1]>370):
		if(rate>50):
			if((rate%2)==0):
				b=center[1]
				r=rate
			if((rate%2)>0):
				a=center[1]
				r=rate
			c=max(a,b)
			r=rate
			if(a>c):
				m=(a,r)
			if(b>c):
				m=(b,r)	
			if(c>=a and c>=b):
				m=(c,r)
	rate=rate+1
	cv2.imshow('frame2',frame)
	cv2.waitKey(2)

cap = cv2.VideoCapture('ball.webm')
for o in range(415):
	ret, frame = cap.read()
	cv2.imshow('frame2',frame)
	cv2.waitKey(1)
	if(o==r):
		
		hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
		#red_up=np.array([180,255,360])
		#red_down=np.array([166,100,80])
		black= np.zeros((480,640,3), np.uint8)
		red_up=np.array([175,255,255])
		red_down=np.array([165,100,100])
		cv2.line(frame,(0,480),(220,370),(0,255,0),2)
		cv2.line(frame,(640,480),(420,370),(0,255,0),2)
		cv2.line(frame,(220,370),(420,370),(0,255,0),2)
		cv2.line(black,(0,480),(220,370),(0,255,0),2)
		cv2.line(black,(640,480),(420,370),(0,255,0),2)
		cv2.line(black,(220,370),(420,370),(0,255,0),2)
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
		img = cv2.circle(frame,center,radius,(255,0,0),2)
		img = cv2.circle(black,center,radius,(255,0,0),2)

		rect = np.array([[220,370],[420,370],[640,480],[0,480]],dtype = "float32")
		dst = np.array([[10,0],[230,0],[230,400],[10,400]],dtype = "float32")
		M = cv2.getPerspectiveTransform(rect, dst)
		warped = cv2.warpPerspective(black, M, (480,640))
		
		blue_up=np.array([0,255,255])
		blue_down=np.array([0,0,0])
	
		mask1=cv2.inRange(warped,blue_down,blue_up)
		mask1 = cv2.erode(mask1, None, iterations=2)
		mask1 = cv2.dilate(mask1, None, iterations=2)
		mask1 = cv2.bitwise_not(mask1)
		#res1=cv2.bitwise_and(warped,warped,mask=mask1)
		the1=cv2.adaptiveThreshold(mask1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,5)
		contours1,hierarchy1 = cv2.findContours(the1, 1, 2)
		cnt1 = contours1[0]
		(x1,y1),radius1 = cv2.minEnclosingCircle(cnt1)
		center1 = (int(x1),int(y1))
		radius1 = int(radius1)
		img1 = cv2.circle(warped,center1,radius1,(255,0,0),2)
		cv2.imshow('frame2',frame)
		cv2.imshow('frame',black)
		cv2.imshow('feame1',warped)

		cv2.waitKey(100000)
