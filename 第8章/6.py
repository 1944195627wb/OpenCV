#通用形态学函数
#dst = cv2.morphologyEx(src,op,kernel[,anchor[,iterations[,borderType[,borderValue])
#开运算——去噪，计数
import cv2
import numpy as np
img = cv2.imread("D:/photo/cat2.webp")
k = np.ones((10,10),np.uint8)
r = cv2.morphologyEx(img,cv2.MORPH_OPEN,k)
cv2.imshow("img",img)
cv2.imshow("result",r)
cv2.waitKey()
cv2.destroyAllWindows()

