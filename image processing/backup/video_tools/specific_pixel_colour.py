import numpy as np
import cv2

img = cv2.imread('ball.jpg',1)

#rect = np.array([[533,186],[791,214],[863,493],[436,457]],dtype = "float32")
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
print hsv[378,481]
#dst = np.array([[0,0],[600,0],[600,730],[0,730]],dtype = "float32")
#M = cv2.getPerspectiveTransform(rect, dst)
#warped = cv2.warpPerspective(img, M, (600,730))
#dst = cv2.warpPerspective(img,img,m,(1024,576))
#cv2.imshow('frame2',warped)
#cv2.imwrite('scan2.jpg',warped)
#cv2.waitKey(100000)
