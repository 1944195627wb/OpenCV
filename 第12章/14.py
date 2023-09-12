#最小包围矩形框
#retval = cv2.minAreaRect(points)
#points= cv2.boxPoints(box)
import cv2
import numpy as np
o = cv2.imread("D:/photo/wen.webp",0)
cv2.imshow("original",o)
ret,binary =cv2.threshold(o,127,255,cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
rect = cv2.minAreaRect(contours[0])
print("rect:\n",rect)
points = cv2.boxPoints(rect)
print("points",points)
points =np.intp(points)
image = cv2.drawContours(o,[points],0,(255,255,255),2)
cv2.imshow("result",o)
cv2.waitKey()
cv2.destroyAllWindows()