#Laplacian算子
#计算像素点P5的近似导数值
#P5lap=（P2+P4+P6+P8）-4·P5
#dst = cv2.Laplacian(src,ddepth[,ksize[,scale[,delta[,borderType]]]])
import cv2
o = cv2.imread("D:/photo/5.jpg",0)
Laplacian = cv2.Laplacian(o,cv2.CV_64F)
Laplacian = cv2.convertScaleAbs(Laplacian)
cv2.imshow("original",o)
cv2.imshow("Laplacian",Laplacian)
cv2.waitKey()
cv2.destroyAllWindows()