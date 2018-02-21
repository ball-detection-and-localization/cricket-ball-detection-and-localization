import cv2
import numpy as np
import colorsys
import time
import argparse
u=0
c=0
key=0
loc=[]
loc1=[]
replay=[]
loc1.append(0)
ratecount=0
f= open("throw2.txt","w+")
replaycount=0
cap = cv2.VideoCapture('throw2.webm')
def count():
	global c
	c=c+1

corner=[]	
# callback
def draw_circle(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		count()
		global corner
		if c==1:
			global x1
			global y1
			cv2.circle(frame,(x,y), 1,(255,0,0),-1)
			x1=x
			y1=y
			cv2.line(frame,(x,y),(x1,y1),(255,0,255),2)
			
			corner.append([x,y])
			
		if c==2:
			cv2.line(frame,(x1,y1),(x,y),(255,0,255),2)
			cv2.circle(frame,(x,y), 1,(255,0,0),-1)
			x1=x
			y1=y
			corner.append([x,y])

		if c==3:
			cv2.line(frame,(x,y),(x1,y1),(255,0,255),2)
			cv2.circle(frame,(x,y), 1,(255,0,0),-1)
			x1=x
			y1=y
			corner.append([x,y])

		if c==4:
			cv2.line(frame,(x,y),(x1,y1),(255,0,255),2)
			cv2.circle(frame,(x,y), 1,(255,0,0),-1)
			x1=x
			y1=y
			corner.append([x,y])
		cv2.imshow('image', frame)
		cv2.waitKey(0)

#  Image
cv2.namedWindow('image')
one=1
while(1):
	if cv2.waitKey(0) & 0xFF == 27:
		one=1
	while(one==1):
		ret, frame = cap.read()
		cv2.namedWindow('image')
		cv2.setMouseCallback('image', draw_circle)
		cv2.imshow('image', frame)
		one=2
	if c>=4:
		break

	cv2.waitKey(1)

count=0
rate=0
a=[]
b=[]
c=0
cap = cv2.VideoCapture('throw2.webm')
while(rate<500):
	
	
	ret, frame = cap.read()
	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	#red_up=np.array([180,255,360])
	#red_down=np.array([166,100,80])
		
	red_up=np.array([175,255,255])
	red_down=np.array([165,100,100])
	cor1=corner[0]
	x21=cor1[0]
	y21=cor1[1]
	cor2=corner[1]
	x22=cor2[0]
	y22=cor2[1]
	cor3=corner[2]
	x23=cor3[0]
	y23=cor3[1]
	cor4=corner[3]
	x24=cor4[0]
	y24=cor4[1]
	cv2.line(frame,(x21,y21),(x22,y22),(0,255,0),2)
	cv2.line(frame,(x22,y22),(x23,y23),(0,255,0),2)
	cv2.line(frame,(x21,y21),(x24,y24),(0,255,0),2)
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
	
	loc.append(center[1])
	if(loc[rate]!= 239):
		replay.append(center)
		replaycount=replaycount+1
	if (loc[rate]>y22):
		if(loc[rate]!= 239):
			if (key==0):
				ratecount=ratecount+1
				loc1.append(loc[rate])
				if (loc1[ratecount-1]<loc1[ratecount]):
					r=rate
				if(loc1[ratecount-1]>loc1[ratecount]):
					key=1
		
	rate=rate+1
	cv2.imshow('frame2',frame)
	cv2.waitKey(2)

cap = cv2.VideoCapture('throw2.webm')
for o in range(503):
	ret, frame1 = cap.read()
	#cv2.imshow('frame2',frame1)
	#r=m[1]
	#cv2.waitKey(1)
	if(o==r):
		hsv1=cv2.cvtColor(frame1,cv2.COLOR_BGR2HSV)
		#red_up=np.array([180,255,360])
		#red_down=np.array([166,100,80])
		black= np.zeros((480,640,3), np.uint8)
		black1= np.zeros((480,640,3), np.uint8)
		red_up=np.array([175,255,255])
		red_down=np.array([165,100,100])
		cv2.line(frame,(x21,y21),(x22,y22),(0,255,0),2)
		cv2.line(frame,(x22,y22),(x23,y23),(0,255,0),2)
		cv2.line(frame,(x21,y21),(x24,y24),(0,255,0),2)
		cv2.line(black,(x21,y21),(x22,y22),(0,255,0),2)
		cv2.line(black,(x22,y22),(x23,y23),(0,255,0),2)
		cv2.line(black,(x21,y21),(x24,y24),(0,255,0),2)
		cv2.line(black1,(x21,y21),(x22,y22),(0,255,0),2)
		cv2.line(black1,(x22,y22),(x23,y23),(0,255,0),2)
		cv2.line(black1,(x21,y21),(x24,y24),(0,255,0),2)
		mask=cv2.inRange(hsv1,red_down,red_up)
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

		rect = np.array([corner[0],corner[1],corner[2],corner[3]],dtype = "float32")
		dst = np.array([[0,0],[120,0],[120,600],[0,600]],dtype = "float32")
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
		d=center1[1]
		d=d
		print d
		landed=(30*0.065*640)/(radius*2*24)*100
		print landed
		f.write(' (1)%d \r\n' %(landed))
		f.write(' (1)%d' %(d))

		
rate=0
while(rate<replaycount-2):
		img1 = cv2.circle(black1,replay[rate],10,(255,0,0),2)
		rate=rate+1
		cv2.line(black1,(replay[rate]),replay[rate-1],(0,255,0),2)
		


cv2.imshow('frame2',frame)
cv2.imshow('frame',black)
cv2.imshow('feame1',warped)
cv2.imshow('feame3',black1)
cv2.waitKey(100000)
