#图像分割与提取
#分水岭算法
#cv2.watershed()
#cv2.distanceTransform()
#cv2.connectedComponents()
#形态学变换
import cv2
import numpy as np
import matplotlib.pyplot as plt
o = cv2.imread("D:/photo/hand.png")
k = np.ones((5,5),np.uint8)
e = cv2.erode(o,k)
b = cv2.subtract(o,e)
plt.subplot(131)
plt.imshow(o)
plt.axis('off')
plt.subplot(132)
plt.imshow(e)
plt.axis('off')
plt.subplot(133)
plt.imshow(b)
plt.axis('off')
plt.show()