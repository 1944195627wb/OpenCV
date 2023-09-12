#霍夫圆环变换
#circles = cv2.HoughCircles(image,method,dp,minDist,param1,param2,minRadius,maxRadius)
#八位的单通道灰度图像
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("D:/photo/22.jpg",0)
imgo = cv2.imread("D:/photo/22.jpg",-1)
o = cv2.cvtColor(imgo,cv2.COLOR_BGR2RGB)
show = o.copy()
img = cv2.medianBlur(img,5)
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,300,param1=50,param2=30,minRadius=100,maxRadius=200)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(o,(i[0],i[1]),i[2],(255,0,0),12)
    cv2.circle(o,(i[0],i[1]),2,(255,0,0),12)
plt.subplot(121)
plt.imshow(show)
plt.axis('off')
plt.subplot(122)
plt.imshow(o)
plt.axis('off')
plt.show()