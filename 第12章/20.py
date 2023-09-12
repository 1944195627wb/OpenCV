#凸包
#hull = cv2.convexHull(points[,clockwise[,returnPoints]])
import cv2
o = cv2.imread("D:/photo/wen.webp",0)
ret,binary = cv2.threshold(o,127,255,cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
hull = cv2.convexHull(contours[1])
print("returnPoints为默认值True时返回值hull的值：\n",hull)
hull2 = cv2.convexHull(contours[1],returnPoints=False)
print("False时hull=",hull2)
