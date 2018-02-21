import cv2
import numpy as np
cap=cv2.VedioCapture(0)
frame=cap.read()
cv2.imshow('frame',frame)

k=cv2.waitKey(5)& 0xFF
if k== 27:
 break
cv2.destroyAllWIndows()
