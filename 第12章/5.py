#计算轮廓的面积——contourArea函数
#retval = cv2.contourArea(contour[,oriented])
import cv2
import numpy as np
o = cv2.imread("D:/photo/wen.webp")
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
ret,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow("original",o)
n = len(contours)
contours_img = []
for i in range(n):
    print("contours["+str(i)+"]面积=",cv2.contourArea(contours[i]))
    temp = np.zeros(o.shape,np.uint8)
    contours_img.append(temp)
    contours_img[i] = cv2.drawContours(contours_img[i],contours,i,(255,255,255),3)
    cv2.imshow("contours["+str(i)+"]",contours_img[i])
cv2.waitKey()
cv2.destroyAllWindows()