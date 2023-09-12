#方向——获取边缘信息
#x->dx=1,dy=0
#y->dx=0,dy=1
#x,y->dx=1,dy=1
#x,y边缘叠加
# dx=cv2.Sobel（src ,ddepth ,1 ,0）
# dy=cv2.Sobel（src ,ddepth ,0 ,1）
# dst=cv2.addWeighted（src1 ,alpha ,src2 ,beta ,gamma）
import cv2
o = cv2.imread("D:/photo/cat2.webp")
Sobelx = cv2.Sobel(o,-1,1,0)
cv2.imshow("original",o)
cv2.imshow("x",Sobelx)
cv2.waitKey()
cv2.destroyAllWindows()