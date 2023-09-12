import cv2
import numpy as np
img = np.zeros((8,8),dtype=np.uint8)
print("img=\n",img)
cv2.imshow("one",img)
print("读取像素点img[3,3]=",img[3,3])
img[3,3]=255
print("修改后img=\n",img)
print("读取修改后像素点img[3,3]=",img[3,3])
cv2.imshow("two",img)
cv2.waitKey()
cv2.destroyAllWindows()
