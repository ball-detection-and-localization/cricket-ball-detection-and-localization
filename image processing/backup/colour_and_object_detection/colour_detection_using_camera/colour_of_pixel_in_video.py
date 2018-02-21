import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while(1):
	_,frame=cap.read()
	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	cv2.imshow('frame',hsv)
	print hsv[1,1]
	cv2.waitKey(100)
