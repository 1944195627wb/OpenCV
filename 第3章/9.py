import cv2
import numpy as np
img1 = cv2.imread("D:/photo/1.png",1)
img2 = np.zeros(img1.shape,dtype=np.uint8)
img2[100:800,100:700] = 255
img3 = cv2.bitwise_and(img1,img2)
print("img1.shape=",img1.shape)
print("img2.shape=",img2.shape)
cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.imshow("img3",img3)
cv2.waitKey()
cv2.destroyAllWindows()
