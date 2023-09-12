#最优拟合直线
#line =cv2.fitLine(points,distType,param,reps,aeps)
import cv2
o = cv2.imread("D:/photo/wen.webp",0)
cv2.imshow("original",o)
ret,binary = cv2.threshold(o,127,255,cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
rows,cols =o.shape[:2]
[vx,vy,x,y] = cv2.fitLine(contours[0],cv2.DIST_L2,0,0.01,0.01)
lefty =int((-x*vy/vx)+y)
righty = int(((cols-x)*vy/vx)+y)
cv2.line(o,(cols-1,righty),(0,lefty),(0,0,255),2)
cv2.imshow("result",o)
cv2.waitKey()
cv2.destroyAllWindows()
