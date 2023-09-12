import cv2
import numpy as np
o = cv2.imread("D:/photo/R.png")
kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(o,kernel,iterations=9)
cv2.imshow("original",o)
cv2.imshow("dilation",dilation)
cv2.waitKey()
cv2.destroyAllWindows()