#计算Hausdorff距离
#h(A,B) = max*min||a-b||(a∈A，b∈B)
#retval = cv2.createHausdorffDistanceExtractor([,distanceFlag[,rankProp])
import cv2
o = cv2.imread("D:/photo/wen.webp")
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
ret,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
for i in range(3):
    o = cv2.drawContours(o,contours[i],-1,(255,255,0),3)
    cv2.imshow(f"{i}",o)
hd = cv2.createHausdorffDistanceExtractor()
d1 = hd.computeDistance(contours[0],contours[0])
d2 = hd.computeDistance(contours[0],contours[1])
d3 = hd.computeDistance(contours[0],contours[2])
print("d1=",d1)
print("d2=",d2)
print("d3",d3)
cv2.waitKey()
cv2.destroyAllWindows()