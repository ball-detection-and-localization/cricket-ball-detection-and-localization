import cv2
import numpy as np
import colorsys
import time
import argparse
u=0
c=0
count=0
cap = cv2.VideoCapture('outside5.webm')
while(1):
	ret, frame = cap.read()
	count=count+1
	print count
	cv2.imshow('frame',frame)
	cv2.waitKey(1)
