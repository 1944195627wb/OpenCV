#利用形状场景算法比较轮廓
#retval = cv2.createShapeContextDistanceExtractor()——计算形状场景距离
#retval=cv2.ShapeDistanceExtractor.computeDistance（contour1,contour2）——计算不同形状之间的距离
import cv2
o = cv2.imread("D:/photo/wen.webp")
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
ret,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cnt1 = contours[0]
cnt2 = contours[1]
cnt3 = contours[2]
sd = cv2.createShapeContextDistanceExtractor()
d1 = sd.computeDistance(cnt1,cnt1)
d2 = sd.computeDistance(cnt1,cnt2)
d3 = sd.computeDistance(cnt1,cnt3)
o = cv2.drawContours(o,cnt1,-1,[255,255,0],2)
cv2.imshow("cnt1",o)
o = cv2.drawContours(o,cnt2,-1,[255,255,0],2)
cv2.imshow("cnt2",o)
o = cv2.drawContours(o,cnt3,-1,[255,255,0],2)
cv2.imshow("cnt3",o)
print("与自身的距离d1=",d1)
print("cnt1和cnt2的距离=",d2)
print("cnt1和cnt2的距离=",d3)
cv2.waitKey()
cv2.destroyAllWindows()
