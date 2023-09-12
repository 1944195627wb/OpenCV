#形态学梯度运算——获得原始图像的边缘
import cv2
import numpy as np
o = cv2.imread("D:/photo/cat2.webp")
k = np.ones((5,5),np.uint8)
r = cv2.morphologyEx(o,cv2.MORPH_GRADIENT,k)
cv2.imshow("original",o)
cv2.imshow("result",r)
cv2.waitKey()
cv2.destroyAllWindows()