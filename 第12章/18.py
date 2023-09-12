#最小外包三角形
#retval,triangle = cv2.minEnclosingTriangle(points)
import cv2
o =cv2.imread("D:/photo/wen.webp",0)
ret,binary = cv2.threshold(o,127,255,cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
area,trgl = cv2.minEnclosingTriangle(contours[0])
print("area",area)
print("trgl:",trgl)
for i in range(3):
    cv2.line(o,tuple(int(x) for x in trgl[i][0]),tuple(int(x) for x in trgl[(i+1) % 3][0]),(255,255,255),2)
cv2.imshow("result",o)
cv2.waitKey()
cv2.destroyAllWindows()
