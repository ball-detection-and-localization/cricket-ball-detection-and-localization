import cv2
import numpy as np
import colorsys
import time
import argparse
u=0
c=0
cap = cv2.VideoCapture('ball.webm')
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
	if c==5:
		break
	cv2.imshow('frame',frame)
	cv2.waitKey(1)
print corner[0]
