#图像平滑处理——将不在其附近区间的的点改成区间内的值
#均值滤波——以当前像素点N*N的均值代替像素值（中间）——角落则以(1-N)*(1-N)
#K = 1/M*N(M为高度N为宽度)
#均值滤波函数 cv2.blur()
#dst = cv2.blur(src,ksize,anchor,borType)
import cv2
o = cv2.imread("D:/photo/16.jpg")
r = cv2.blur(o,(5,5))
cv2.imshow("original",o)
cv2.imshow("result",r)
cv2.waitKey()
cv2.destroyAllWindows()
