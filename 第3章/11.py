#利用cv2.bitwise_and中的mask参数进行掩模
import cv2
import numpy as np
img = cv2.imread("D:/photo/1.png",1)
w,h,c = img.shape
mask = np.zeros((w,h),dtype=np.uint8)
mask[100:800,100:700] = 255#可以是任何数，在不是0处进行运算
img2 = cv2.bitwise_and(img,img,mask=mask)#必须是(mask=mask)
print("img.shape=",img.shape)
print("mask.shape=",mask.shape)
cv2.imshow("img",img)
cv2.imshow("mask",mask)
cv2.imshow("img2",img2)
cv2.waitKey()
cv2.destroyAllWindows()

