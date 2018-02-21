import cv2
import numpy as np
import colorsys
import time
import argparse
u=0
#def line(lastmidx,midy):
#	b=1
#	while(u==0):
#		if(b==1):
#			lastmidx=lastmidx+1
#			if(mask[lastmidx,midy]==0):
#				b=2
#				pintx=mask[lastmidx,midy]

one=1
cap = cv2.VideoCapture('ball.webm')
while(1):
	if cv2.waitKey(0) & 0xFF == 27:
		one=1
	while(one==1):
		ret, frame = cap.read()

		#frame = cv2.imread('pitch.jpg',1)
		#frame=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
		black_up=np.array([110,110,110])
		black_down=np.array([0,0,0])
		#black_up=np.array([180,250,250])
		#black_down=np.array([0,0,0])
		#cv2.line(frame,(0,480),(220,370),(0,255,0),2)
		#cv2.line(frame,(640,480),(420,370),(0,255,0),2)
		#cv2.line(frame,(220,370),(420,370),(0,255,0),2)
		mask=cv2.inRange(frame,black_down,black_up)
		mask = cv2.erode(mask, None, iterations=2)
		mask = cv2.dilate(mask, None, iterations=2)
		res=cv2.bitwise_and(frame,frame,mask=mask)
		the=cv2.adaptiveThreshold(mask,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,5,5)
		contours,hierarchy = cv2.findContours(the, 1, 2)
		cnt = contours[0]
		print cnt
		leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
		rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
		#topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
		#bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
		#(x,y),radius = cv2.minEnclosingCircle(cnt)
		#center = (int(x),int(y))
		#radius = int(radius)
		#img = cv2.circle(frame,center,radius,(255,0,0),2)
		cv2.line(frame,leftmost,rightmost,(255,0,255),2)
		lastmidx=(leftmost[0]+rightmost[0])/2
		lastmidy=(leftmost[1]+rightmost[1])/2
		l=0
		#for y in range(10,600):
		#	print y
		#	midy=lastmidy-y-l
		#	if(midy==0):
		#		break
		#	if(mask[lastmidx,midy]==255):
		#		midy1= mask[lastmidx,midy]
		#		midy= mask[lastmidx,midy]
		#		l=line(lastmidx,midy1)
		cv2.imshow('frame',frame)
		cv2.imshow('feame',mask)
		one=2
	cv2.waitKey(1)
