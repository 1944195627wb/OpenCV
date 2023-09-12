#几何学测试
#1.测试轮廓是否凸型
#retval = cv2.isContourConvex(contour)
import cv2
o = cv2.imread("D:/photo/hand.png",0)
ret,binary = cv2.threshold(o,127,255,cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

image1 = o.copy()
hull = cv2.convexHull(contours[0])
cv2.polylines(image1,[hull],True,(255,255,0),2)
print("使用函数cv2.convexHull()构造的多边形是否是凸形的：",cv2.isContourConvex(hull))
cv2.imshow("result1",image1)

image2 = o.copy()
epsilon = 0.005*cv2.arcLength(contours[0],True)
approx = cv2.approxPolyDP(contours[0],epsilon,True)
image2 = cv2.drawContours(image2,[approx],0,(0,0,255),2)
print("使用函数cv2.approxPolyDP()构造的多边形是否是凸形的：",cv2.isContourConvex(approx))
cv2.imshow("result2",image2)

cv2.waitKey()
cv2.destroyAllWindows()