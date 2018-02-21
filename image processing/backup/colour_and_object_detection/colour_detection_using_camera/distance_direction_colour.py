import cv2
import numpy as np
import colorsys
from numpy import interp
import time
cap=cv2.VideoCapture(0)
x=0
b=0
c=0
f= open("trialdata.txt","w+")
count=0
dot=[0,0]
def movement(b,c):
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
	img = cv2.circle(frame,center,radius,(255,0,0),2)
	rad=(30*0.065*640)/(radius*2*24)*100
	print rad
	font = cv2.FONT_HERSHEY_SIMPLEX
	if(b==1):
		cv2.putText(frame,'A',(400,70), font, 4,(255,0,0),2)

	if(b==2):
		cv2.putText(frame,'V',(400,70), font, 4,(255,0,0),2)

	if(c==1):
		cv2.putText(frame,'<-',(450,70), font, 4,(255,0,0),2)

	if(c==2):
		cv2.putText(frame,'->',(450,70), font, 4,(255,0,0),2)

	cv2.imshow('frame2',frame)
	cv2.waitKey(2)
	return x,y

def plot(loc,loc3):
	
	a=abs(loc[0]-loc3[0])*0.34
	b=a/125*100
	print b,'cm per seconds'
	f.write('(%f mm per second \n \r ' %(b))
	if (loc[0]>loc3[0]):
		b=1
	else:
		b= 2
	
	if (loc[1]>loc3[1]):
		c=1
	else:	
		c=2
	return b,c

def gap(b,c):
	for q in range (62):
		w=movement(b,c)
	

while(1):
	count=count+1
	loc=movement(b,c)
	gap(b,c)
	loc3=movement(b,c)
	b,c=plot(loc,loc3)
	
	
