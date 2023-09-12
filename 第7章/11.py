#2D卷积
#dst = cv2.filter2D(src,ddepth,kernel,anchor,delta,borderType)
import cv2
import numpy as np
o = cv2.imread("D:/photo/1.png")
kernel = np.ones((9,9),np.float32)/81
r = cv2.filter2D(o,-1,kernel)
cv2.imshow("original",o)
cv2.imshow("Gaussian",r)
cv2.waitKey()
cv2.destroyAllWindows()