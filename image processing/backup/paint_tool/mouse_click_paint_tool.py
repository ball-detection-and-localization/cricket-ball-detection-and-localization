import cv2

import numpy as np
c=0
def count():
	global c
	c=c+1
	if(c>3):
		c=2
# callback
def draw_circle(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		count()
		if c==1:
			global x1
			global y1
			cv2.circle(img,(x,y), 1,(255,0,0),-1)
			x1=x
			y1=y
			cv2.line(img,(x,y),(x1,y1),(255,0,255),2)
			
		if c==2:
			cv2.line(img,(x1,y1),(x,y),(255,0,255),2)
			cv2.circle(img,(x,y), 1,(255,0,0),-1)
			x1=x
			y1=y

		if c==3:
			cv2.line(img,(x,y),(x1,y1),(255,0,255),2)
			cv2.circle(img,(x,y), 1,(255,0,0),-1)
			x1=x
			y1=y

		cv2.imshow('image', img)
		cv2.waitKey(0)

#  Image

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
while(1):
	

	cv2.setMouseCallback('image', draw_circle)

	cv2.imshow('image', img)

	if cv2.waitKey(0) & 0xFF == 27:

		break


cv2.destroyAllWindows()
