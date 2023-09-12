#闭运算
import cv2
import numpy as np
img = cv2.imread("D:/photo/cat.webp")
k = np.ones((10,10),np.uint8)
r = cv2.morphologyEx(img,cv2.MORPH_CLOSE,k)
cv2.imshow("img",img)
cv2.imshow("result",r)
cv2.waitKey()
cv2.destroyAllWindows()