#Solidity
#Solidity =轮廓面积（对象面积）/凸包面积
import cv2
o = cv2.imread("D:/photo/wen.webp")
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
ret,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
o = cv2.drawContours(o,contours[0],-1,(255,255,0),2)
cntArea= cv2.contourArea(contours[0])
hull =cv2.convexHull(contours[0])
hullArea = cv2.contourArea(hull)
cv2.polylines(o,[hull],True,(255,0,0),2)
solidity = float(cntArea)/hullArea
print(solidity)
cv2.imshow("result",o)
cv2.waitKey()
cv2.destroyAllWindows()
