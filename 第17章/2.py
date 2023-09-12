#距离变换函数distanceTransform
#如果前景对象的中心（质心）距离值为0的像素点距离较远，会得到一个较大的值
#如果前景对象的边缘距离值为0的像素点较近，会得到一个较小的值
#dst = cv2.distanceTransform(src,distanceType,maskSize[,dstType]])
import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread("D:/photo/R.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
show = img.copy()
ret,thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
kernel = np.ones((3,3),np.uint8)
opening =cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=2)
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret_,fore = cv2.threshold(dist_transform,0.4*dist_transform.max(),255,0)
plt.subplot(131)
plt.imshow(show)
plt.axis('off')
plt.subplot(132)
plt.imshow(dist_transform)
plt.axis('off')
plt.subplot(133)
plt.imshow(fore)
plt.axis('off')
plt.show()