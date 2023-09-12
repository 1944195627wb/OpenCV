#平均颜色及平均灰度
#mean_val = cv2.mean(im,mask=mask)
import cv2
import numpy as np
o = cv2.imread("D:/photo/5.jpg")
cv2.imshow("original",o)
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
ret,binary =cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
mask = np.zeros(gray.shape,np.uint8)
cv2.drawContours(mask,[cnt],0,(255,255,255),-1)
meanval =cv2.mean(o,mask=mask)
print(meanval)
masko =np.zeros(o.shape,np.uint8)
cv2.drawContours(masko,[cnt],-1,(255,255,255),-1)
loc = cv2.bitwise_and(o,masko)
cv2.imshow("mask",loc)
cv2.imshow("mask",loc)
cv2.waitKey()
cv2.destroyAllWindows()
