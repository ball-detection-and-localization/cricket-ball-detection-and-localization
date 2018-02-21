#gray = cv2.imread('square2.jpg',1)
	#_,gray=cap.read()
	#imgray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
	#ret, thresh = cv2.threshold(imgray, 100, 255, cv2.THRESH_BINARY_INV)
	#the=cv2.adaptiveThreshold(thresh,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,5)
	#contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	#cv2.drawContours(gray, contours, -1, (0,255,0), 3)
	#cnt = contours[0]
	#x,y,w,h = cv2.boundingRect(cnt)
	#cv2.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),2)
	#rad=(30*0.06*480)/(h*24)*100
	#rad=w*0.34
	#print rad



import numpy as np
import cv2

img = cv2.imread('square1.jpg',1)
m=np.matrix([[0,1024,100],[0,576,100],[0,0,1]])

rect = np.array([[90,93],[375,13],[404,413],[96,414]],dtype = "float32")
d1=((90-375)**2+(93-13)**2)**0.5
d2=((96-404)**2+(414-413)**2)**0.5
d3=((414-93)**2+(90-96)**2)**0.5
d4=((375-404)**2+(413-13)**2)**0.5
maxWidth = max(int(d1), int(d2))
maxHeight = min(int(d3), int(d4))
dst = np.array([[20,20],[maxWidth-1+20,20],[maxWidth+20, maxHeight+20],[20,maxHeight-1+20]],dtype = "float32")
M = cv2.getPerspectiveTransform(rect, dst)
print M
warped = cv2.warpPerspective(img, M, (maxWidth+40, maxHeight+40))
#dst = cv2.warpPerspective(img,img,m,(1024,576))
cv2.imshow('frame2',warped)
cv2.waitKey(100000)
