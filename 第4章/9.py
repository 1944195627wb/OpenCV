#提取颜色时区间半径大概10
# ● 蓝色：值分布在[110,100,100]和[130,255,255]之间。
# ● 绿色：值分布在[50,100,100]和[70,255,255]之间。
# ● 红色：值分布在[0,100,100]和[10,255,255]之间。
import cv2
import numpy as np
img = cv2.imread("D:/photo/5.jpg")
hsv =cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("img",img)
minBlue = np.array([100,50,50])
maxBlue = np.array([150,255,255])
mask = cv2.inRange(hsv,minBlue,maxBlue)
blue = cv2.bitwise_and(img,img,mask=mask)
cv2.imshow("blue",blue)

minGreen = np.array([50,50,50])
maxGreen = np.array([70,255,255])
mask = cv2.inRange(hsv,minGreen,maxGreen)
green =cv2.bitwise_and(img,img,mask=mask)
cv2.imshow("green",green)

minRed = np.array([0,50,50])
maxRed = np.array([30,255,255])
mask = cv2.inRange(hsv,minRed,maxRed)
red = cv2.bitwise_and(img,img,mask=mask)
cv2.imshow("red",red)
cv2.waitKey()
cv2.destroyAllWindows()