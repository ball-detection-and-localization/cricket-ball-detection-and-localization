import numpy as np
import cv2

gray = cv2.imread('lotus.jpg',1)
green=0
red=0
blue=0
for x in range(479):
	for y in range(639):
		val=gray[x,y]
		green=val[1]+green
		red=val[0]+red
		blue=val[2]+blue
green=green/307200
red=red/307200
blue=blue/307200
for x in range(575):
	for y in range(1023):
		val=gray[x,y]
		green1=abs(val[1]-green)
		red1=abs(val[0]-red)
		blue1=abs(val[2]-blue)
		if(green1<0):
			green1=255
		if(red1<0):
			red1=255
		if(blue1<0):
			blue1=255
		gray[x,y]=[red1,green1,blue1]

#imgray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
#ret, thresh = cv2.threshold(gray, 127, 255, 0)
#contours, hierarchy = cv2.findContours(thresh, 1,2)

#cv2.drawContours(gray, contours, -1, (0,255,0), 3)
cv2.imshow('frame2',gray)
cv2.waitKey(100000)
