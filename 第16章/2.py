#HoughLinesP函数
#lines = cv2.HoughLinesP(image,rho,theta,threshold,minLineLength,maxLineGap)
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("D:/photo/zhi.png",-1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edge = cv2.Canny(gray,50,150,apertureSize=3)
org = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
show = org.copy()
lines = cv2.HoughLinesP(edge,1,np.pi/180,1,minLineLength=10,maxLineGap=10)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(org,(x1,y1),(x2,y2),(255,0,255),5)
plt.subplot(121)
plt.imshow(show)
plt.axis('off')
plt.subplot(122)
plt.imshow(org)
plt.axis('off')
plt.show()