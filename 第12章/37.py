#最大值和最小值及他们的位置
#min_val,max_val,min_loc,max_loc=cv2.minMaxLoc（imgray,mask=mask）
import cv2
import numpy as np
o = cv2.imread("D:/photo/7.webp")
cv2.imshow("original",o)
gray=cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
ret,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cnt =contours[0]
mask = np.zeros(gray.shape,np.uint8)
mask = cv2.drawContours(mask,[cnt],-1,(255,255,0),-1)
minval,maxval,minloc,maxloc= cv2.minMaxLoc(gray,mask=mask)
print(minval)
print(maxval)
print(minloc)
print(maxloc)
masko = np.zeros(o.shape,np.uint8)
masko = cv2.drawContours(masko,[cnt],-1,(255,255,255),-1)
loc = cv2.bitwise_and(o,masko)
cv2.imshow("mask",loc)
loc= cv2.bitwise_and(gray,mask)
cv2.imshow("mask",loc)
cv2.waitKey()
cv2.destroyAllWindows()
