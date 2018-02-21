import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame##### conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    ret, gray = cap.read()
   # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Our operations on the frame come here
   # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    data=[]
    point=[]
    a=[]
    b=[]
    c=[]
    d=[]
    lower_blue = np.array([0,0,50])
    upper_blue = np.array([130,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(gray, lower_blue, upper_blue)
    fil = cv2.GaussianBlur(gray.copy(), (5, 5), 8)
    # Bitwise-AND mask and original image ##### 
    res = cv2.bitwise_and(gray,gray, mask= mask)

   
  #  print w,h
   # for x in range(240):
	# for y in range (319):
         #    c=res[x*2,y*2]
          #   res[x,y]=c
	#     if (c>100):
         #       cv2.circle(gray,(y,x),1,(0,255,0),1,8)
   # roi = res[0:239,0:319]	     
   # new=np.zeros((480,640,3),np.uint8)
   # for y in range(319):
    #     for x in range (239):
     #       d=roi[x,y]-gray[x+1,y]
      #      if (d>200):
       #        cv2.circle(gray,(y,x),0,(0,255,0),1,8)
    #w,h=roi.shape[::1]
    #print w,h
 
    cv2.imshow('frame',fil)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
