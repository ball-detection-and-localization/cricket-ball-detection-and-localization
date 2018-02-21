import numpy as np
import cv2

img = cv2.imread('lotus.jpg',1)
m=np.matrix([[0,1024,100],[0,576,100],[0,0,1]])

rect = np.array([[533,186],[791,214],[863,493],[436,457]],dtype = "float32")

dst = np.array([[0,0],[600,0],[600,730],[0,730]],dtype = "float32")
M = cv2.getPerspectiveTransform(rect, dst)
warped = cv2.warpPerspective(img, M, (600,730))
#dst = cv2.warpPerspective(img,img,m,(1024,576))
cv2.imshow('frame2',warped)
#cv2.imwrite('scan2.jpg',warped)
cv2.waitKey(100000)
