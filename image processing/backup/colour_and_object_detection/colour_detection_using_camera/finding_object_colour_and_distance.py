import cv2
import numpy as np
import colorsys
from numpy import interp
import time

cap=cv2.VideoCapture(0)
i=5
f= open("testdata.txt","w+")
while(1):
	_,frame=cap.read()
	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	blue_up=np.array([125,255,255])
	blue_down=np.array([105,70,100])
	
	red_up=np.array([180,255,360])
	red_down=np.array([166,100,80])

	green_up=np.array([60,255,255])
	green_down=np.array([40,90,80])

	yellow_up=np.array([39,255,255])
	yellow_down=np.array([21,100,0])

	pink_up=np.array([165,255,255])
	pink_down=np.array([145,100,0])

	red1_up=np.array([4,255,255])
	red1_down=np.array([0,160,0])

	six_up=np.array([290,160,300])
	six_down=np.array([290,160,300])
       
	
			
	mask=cv2.inRange(hsv,blue_down,blue_up)
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

			
	mask1=cv2.inRange(hsv,red_down,red_up)
	mask1= cv2.erode(mask1, None, iterations=2)
	mask1= cv2.dilate(mask1, None, iterations=2)
	res1=cv2.bitwise_and(frame,frame,mask=mask1)
	the1=cv2.adaptiveThreshold(mask1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,5)
	contours1,hierarchy1 = cv2.findContours(the1, 1, 2)
	cnt1 = contours1[0]
	(x1,y1),radius1 = cv2.minEnclosingCircle(cnt1)
	center1 = (int(x1),int(y1))
	radius1= int(radius1)
	img1 = cv2.circle(frame,center1,radius1,(0,0,255),2)

       
	mask2=cv2.inRange(hsv,green_down,green_up)
	mask2 = cv2.erode(mask2, None, iterations=2)
	mask2 = cv2.dilate(mask2, None, iterations=2)
	res2=cv2.bitwise_and(frame,frame,mask=mask2)
	the2=cv2.adaptiveThreshold(mask2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,5)
	contours2,hierarchy2 = cv2.findContours(the2, 1, 2)
	cnt2 = contours2[0]
	(x2,y2),radius2 = cv2.minEnclosingCircle(cnt2)
	center2 = (int(x2),int(y2))
	radius2 = int(radius2)
	img2 = cv2.circle(frame,center2,radius2,(0,255,0),2)
	
	mask3=cv2.inRange(hsv,yellow_down,yellow_up)
	mask3 = cv2.erode(mask3, None, iterations=2)
	mask3 = cv2.dilate(mask3, None, iterations=2)
	res3=cv2.bitwise_and(frame,frame,mask=mask3)
	the3=cv2.adaptiveThreshold(mask3,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,5)
	contours3,hierarchy3 = cv2.findContours(the3, 1, 2)
	cnt3 = contours3[0]
	(x3,y3),radius3 = cv2.minEnclosingCircle(cnt3)
	center3 = (int(x3),int(y3))
	radius3 = int(radius3)
	img3 = cv2.circle(frame,center3,radius3,(0,255,255),2)
 
	mask4=cv2.inRange(hsv,pink_down,pink_up)
	mask4 = cv2.erode(mask4, None, iterations=2)
	mask4 = cv2.dilate(mask4, None, iterations=2)
	res4=cv2.bitwise_and(frame,frame,mask=mask4)
	the4=cv2.adaptiveThreshold(mask4,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,5)
	contours4,hierarchy4 = cv2.findContours(the4, 1, 2)
	cnt4 = contours4[0]
	(x4,y4),radius4 = cv2.minEnclosingCircle(cnt4)
	center4 = (int(x4),int(y4))
	radius4 = int(radius4)
	img4 = cv2.circle(frame,center4,radius4,(255,0,255),2)
	
	i=0
	k=[10]
	rad=(30*0.0083*480)/(radius*2*24)*100
	rad1=(30*0.0083*480)/(radius1*2*24)*100
	rad2=(30*0.0083*480)/(radius2*2*24)*100
	rad3=(30*0.0083*480)/(radius3*2*24)*100
	rad4=(30*0.083*480)/(radius4*2*24)*100

	#k[i]=center ####### blur = cv2.blur(img,(5,5))
	#i=i+1
	#if(i>9):
		#vel=k[0]
	t0 = time.clock()
	print ('blue found at ',t0)
	f.write('\r \n (1)%d' %(rad))
	f.write('  (2)%d' %(rad1))
	f.write('  (3)%d' %(rad2))
	f.write('  (4)%d' %(rad3))
	f.write('  (5)%d \r\n' %(rad4))
	f.write(str(t0))
        #if ()

	print rad #,rad1,rad2,rad3,rad4
	cv2.imshow('frame',frame)
	cv2.waitKey(5)
