#方框滤波
#1.领域像素值之和的平均值 2.领域像素之和
#dst = cv2.boxFilter(src,ddepth,ksize,anchor,normalize,borderType)
#M = 1/(width*height) (normalize=1) /=1(normalize=0)
import cv2
o = cv2.imread("D:/photo/16.jpg")
r = cv2.boxFilter(o,-1,(5,5))
cv2.imshow("original",o)
cv2.imshow("result",r)
cv2.waitKey()
cv2.destroyAllWindows()