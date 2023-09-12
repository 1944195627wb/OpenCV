#中值滤波——用邻域内所有像素值先排序，中间值来替代当前像素点的像素值
# dst = cv2.medianBlur(src,ksize)(ksize为奇数)
import cv2
o = cv2.imread("D:/photo/16.jpg")
r = cv2.medianBlur(o,3)
cv2.imshow("original",o)
cv2.imshow("result",r)
cv2.waitKey()
cv2.destroyAllWindows()
