#Scharr算子
#dst = cv2.Scharr(src,ddepth,dx,dy[,scale[,delta[,borderType]]])
import cv2
o = cv2.imread("D:/photo/cat2.webp")
Scharrx = cv2.Scharr(o,cv2.CV_64F,1,0)
Scharrx = cv2.convertScaleAbs(Scharrx)
cv2.imshow("original",o)
cv2.imshow("x",Scharrx)
cv2.waitKey()
cv2.destroyAllWindows()