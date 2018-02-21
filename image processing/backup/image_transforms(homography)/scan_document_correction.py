import numpy as np
import cv2

img = cv2.imread('scan.jpg',1)
m=np.matrix([[0,1024,100],[0,576,100],[0,0,1]])

rect = np.array([[0,0],[1700,0],[1700,2338],[0,2338]],dtype = "float32")
d1=((90-375)**2+(93-13)**2)**0.5
d2=((96-404)**2+(414-413)**2)**0.5
d3=((414-93)**2+(90-96)**2)**0.5
d4=((375-404)**2+(413-13)**2)**0.5
maxWidth = max(int(d1), int(d2))
maxHeight = min(int(d3), int(d4))
dst = np.array([[0,0],[1700,70],[1700,2438],[0,2438]],dtype = "float32")
M = cv2.getPerspectiveTransform(rect, dst)
warped = cv2.warpPerspective(img, M, (1700,2398))
#dst = cv2.warpPerspective(img,img,m,(1024,576))
cv2.imshow('frame2',warped)
cv2.imwrite('scan2.jpg',warped)
cv2.waitKey(100000)
