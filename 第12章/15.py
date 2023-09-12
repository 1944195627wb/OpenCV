#最小包围圆形
#center,radius =cv2.minEnclosingCircle(points)
import cv2
o = cv2.imread("D:/photo/wen.webp",0)
ret,binary =cv2.threshold(o,127,255,cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
(x,y),radius = cv2.minEnclosingCircle(contours[0])
center =(int(x),int(y))
radius =int(radius)
cv2.circle(o,center,radius,(255,255,255),2)
cv2.imshow("result",o)
cv2.waitKey()
cv2.destroyAllWindows()