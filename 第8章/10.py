#黑帽运算——用闭运算图像减去原始图像的操作。黑帽运算能够获取图像内部的小孔，或前景色中的小黑点，或者得到比原始图像的边缘更暗的边缘部分
import cv2
import numpy as np
o1 = cv2.imread("D:/photo/cat.webp")
o2 = cv2.imread("D:/photo/cat2.webp")
k = np.ones((5,5),np.uint8)
r1 = cv2.morphologyEx(o1,cv2.MORPH_BLACKHAT,k)
r2 = cv2.morphologyEx(o2,cv2.MORPH_BLACKHAT,k)
cv2.imshow("original1",o1)
cv2.imshow("original2",o2)
cv2.imshow("result1",r1)
cv2.imshow("result2",r2)
cv2.waitKey()
cv2.destroyAllWindows()
