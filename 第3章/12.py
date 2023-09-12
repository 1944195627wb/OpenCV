#cv2.add()可以是图像和图像，也可以是图像和数字，但尺寸和通道必须相同
import cv2
import numpy as np
img1 = np.ones((4,4),dtype=np.uint8)*3
img2 = np.ones((4,4),dtype=np.uint8)*5
print("img1=\n",img1)
print("img2=\n",img2)
img3 = cv2.add(img1,img2)
print("cv2.add(img1,img2)=\n",img3)
img4 = cv2.add(img1,6)
print("cv2.add(img1,6)=\n",img4)
img5 = cv2.add(6,img2)
print("cv2.add(6,img2)=\n",img5)
