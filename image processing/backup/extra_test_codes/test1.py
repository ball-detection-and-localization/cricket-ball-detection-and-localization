import cv2
import numpy as np
import colorsys
x=0
y=0
cap=cv2.VideoCapture(0)
f= open("testdata.txt","w+")
while(1):
	_,frame=cap.read()
	#hsv=cv2.cvtColor(frame,cv2.COLOR_RGB2HSV)
	#hsv=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
	#red_up=np.array([12,255,255])
	#red_down=np.array([0,40,80])
	#whitered_up=np.array([180,50,255])
	#whitered_down=np.array([170,0,170])
	#white_up=np.array([180,50,255])
	#white_down=np.array([0,0,150])
	#cv2.rectangle(frame,(300,230),(340,190),(0,255,0),3)
	img = cv2.circle(frame,(300,230),2,(255,0,0),2)
	#b=0
	#c=0
	#d=0
	#for x in range(479):
	#	for y in range(639):
	#		a=frame[x,y]
	#		b=a[0]+b
	#		c=a[1]+c
	#		d=a[2]+d
	#b=int(b/307200)
	#c=int(c/307200)
	#d=int(d/307200)
	#for x in range(479):
	#	for y in range(639):
	#		a=frame[x,y]
	#		frame[x,y]=(abs(a[0]-b),abs(a[1]-c),abs(a[2]-d))
	#f.write('\r \n (1)%d' %(a[0]))
	#f.write(' (2)%d' %(a[1]))
	#f.write(' (3)%d' %(a[2]))
	H, S, V = cv2.split(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV))
	#S=map(S+100)
	#eq_V = cv2.equalizeHist(V)
	#eq_H = cv2.equalizeHist(S)
	#eq_S = cv2.equalizeHist(H)
	image = cv2.cvtColor(cv2.merge([H,S,V]), cv2.COLOR_HSV2BGR)
	#hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
	#print hsv[230,300]
	#img = cv2.circle(frame,(300,230),2,(255,0,0),2)
	
	cv2.imshow('frame2',image)
	cv2.waitKey(1)
