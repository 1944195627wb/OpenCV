#图像金字塔
#1.先滤波2.删除偶数行和偶数列
#领域滤波器
#高斯滤波器——cv2.pyrDown()——先滤波然后向下采样
#向上采样时，会对新生成的像素点插值
#最邻近插值、补零(右侧和下方)
#dst = cv2.pyrDown(src[,dstsize[,borderType]])
# 默认情况下，输出图像的大小为Size（（src.cols+1）/2,
# （src.rows+1）/2）。在任何情况下，图像尺寸必须满足如下条件：
# |dst.width*2−src.cols|≤2
# |dst.height*2−src.rows|≤2
import cv2
o = cv2.imread("D:/photo/5.jpg")
r1 = cv2.pyrDown(o)
r2 = cv2.pyrDown(r1)
r3 = cv2.pyrDown(r2)
print("o.shape=",o.shape)
print("r1.shape=",r1.shape)
print("r2.shape=",r2.shape)
print("r3.shape=",r3.shape)
cv2.imshow("original",o)
cv2.imshow("r1",r1)
cv2.imshow("r2",r2)
cv2.imshow("r3",r3)
cv2.waitKey()
cv2.destroyAllWindows()


