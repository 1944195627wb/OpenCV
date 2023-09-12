#Extent——轮廓面积和矩形边界面积之比
#Extend=轮廓面积(对象面积)/矩形边界面积
import cv2
o = cv2.imread("D:/photo/wen.webp")
cv2.imshow("original",o)
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
ret,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
x,y,w,h = cv2.boundingRect(contours[0])
cv2.rectangle(o,(x,y),(x+w,y+h),(255,255,0),2)
o = cv2.drawContours(o,contours[0],-1,(0,255,0),2)
rectangleArea =w*h
contours_Area = cv2.contourArea(contours[0])
extend = float(contours_Area)/rectangleArea
print(extend)
cv2.imshow("result",o)
cv2.waitKey()
cv2.destroyAllWindows()