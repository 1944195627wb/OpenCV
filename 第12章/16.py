#最优拟合椭圆
#retval =cv2.fitEllipse(points)
import cv2
o =cv2.imread("D:/photo/wen.webp",0)
ret,binary = cv2.threshold(o,127,255,cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow("original",o)
ellipse =cv2.fitEllipse(contours[0])
print("ellipse",ellipse)
cv2.ellipse(o,ellipse,(255,255,0),3)
cv2.imshow("result",o)
cv2.waitKey()
cv2.destroyAllWindows()