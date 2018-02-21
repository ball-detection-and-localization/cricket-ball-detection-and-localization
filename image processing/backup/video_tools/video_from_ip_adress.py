import cv2
import numpy as np
import colorsys

cap=cv2.VideoCapture('http://192.168.1.22:8080/')

while(1):
	_,frame=cap.read()
	cv2.imshow('frame',frame)
	cv2.waitKey(1000)
