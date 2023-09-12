#霍夫直线——用于检测直线和圆、椭圆等
#在进行霍夫变换之前要先将源图像进行二值化或进行Canny边缘检测
#lines = cv2.HoughLines(image,rho,theta,threshold)
#必须是8位的单通道二值图像
#HoughLines函数
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("D:/photo/zhi.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edge = cv2.Canny(gray,50,150,apertureSize=3)
org = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
show = org.copy()
lines = cv2.HoughLines(edge,1,np.pi/180,140)
for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0+1000*(-b))
    y1 = int(y0+1000*a)
    x2 = int(x0-1000*(-b))
    y2 = int(y0-1000*a)
    cv2.line(org,(x1,y1),(x2,y2),(255,0,255),2)
plt.subplot(121)
plt.imshow(show)
plt.axis('off')
plt.subplot(122)
plt.imshow(org)
plt.axis('off')
plt.show()