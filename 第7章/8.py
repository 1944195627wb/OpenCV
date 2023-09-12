#双边滤波——距离越远，权重越小；色彩差别越大，权重越小
#dst = cv2.bilateralFilter(src,d,sigmaColor,sigmaSpace,borderType)
import cv2
o = cv2.imread("D:/photo/4.jpg")
r = cv2.bilateralFilter(o,25,100,100)
cv2.imshow("original",o)
cv2.imshow("result",r)
cv2.waitKey()
cv2.destroyAllWindows()