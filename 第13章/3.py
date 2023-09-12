#使用opencv绘制直方图
#hist = cv2.calcHist(images,channels,mask,histSize,ranges,accumulate)
import cv2
import numpy as np
img = cv2.imread("D:/photo/5.jpg")
hist = cv2.calcHist([img],[0],None,[256],[0,255])
print(type(hist))
print(hist.shape)
print(hist.size)
print(hist)
