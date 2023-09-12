#数字水印
#最低有效位(二进制中的第0位)
#嵌入过程：将载体图像的第0个位平面替换成数字水印信息
#提取过程：将载体图像的最低有效位所构成的第0个位平面提取出来
#嵌入：(1)原始载体图像预处理——与254提取矩阵进行按位与运算
# (2)水印图像处理(阈值处理)(3)嵌入水印——与水印图像的二值图像进行按位或运算
#提取：(1)提取最低有效位平面(按位与运算)(2)阈值处理(3)提取去水印的图像(与254进行按位与运算)
import cv2
import numpy as np
#读取原始图像
img1 = cv2.imread("D:/photo/6.webp",0)
#读取水印图像
img2 = cv2.imread("D:/photo/7.webp",0)
cv2.imshow("img2",img2)
cv2.waitKey()
#将水印图像内的值255处理为1
w = img2[:,:]>0
img2[w] = 1
#读取原始载体图像的shape值
r,c = img1.shape
#嵌入：
t254 = np.ones((r,c),dtype=np.uint8)*254
#获取img1图像的高7位
img1H7 = cv2.bitwise_and(img1,t254)
#将img2嵌入img1H7内
e = cv2.bitwise_or(img1H7,img2)
#提取：
#生成元素值为1的数组
t1 =np.ones((r,c),dtype=np.uint8)
wm = cv2.bitwise_and(e,t1)
print(wm)
#将水印图像内的值处理为255
w = wm[:,:]>0
wm[w]=255
#显示：
cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.imshow("e",e)
cv2.imshow("wm",wm)
cv2.waitKey()
cv2.destroyAllWindows()