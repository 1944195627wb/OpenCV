#等效直径
#等效直径 = sqrt(4*轮廓面积/Π)
import cv2
import numpy as np
o = cv2.imread("D:/photo/hand.png")
cv2.imshow("original",o)
gary = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
ret,binary = cv2.threshold(gary,127,255,cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(o,contours[0],-1,(225,255,0),2)
cntArea = cv2.contourArea(contours[0])
equiDiameter = np.sqrt(4*cntArea/np.pi)
print(equiDiameter)
cv2.circle(o,(100,100),int(equiDiameter/2),(0,0,255),2)
cv2.imshow("result",o)
cv2.waitKey()
cv2.destroyAllWindows()