#位平面——由像素值中每一个位值所组成的图像
#第i个位平面 从右边数第i个比特位
#对于RGB图像，对每个通道的第i个位平面进行组合则可以产生一副新的彩色图像
#1.获取原始图像的宽和高
#2.构造提取矩阵——2^n提取矩阵以提取第n个位平面
#3.提取位平面——将图像与2^n进行按位与运算
#另一种方法：若提取第n个位平面，则可以将像素向右侧移动n位然后对2进行位运算
#阈值处理——使图像显示更为明显，将其中大于0的值处理为255
#mask = 位平面[:,:,i]>0
#位平面[mask]=255
import cv2
import numpy as np
img = cv2.imread("D:/photo/1.png",0)
cv2.imshow("img",img)
r,c = img.shape
x = np.zeros((r,c,8),dtype=np.uint8)
for i in range(8):
    x[:,:,i] = 2**i
r = np.zeros((r,c,8),dtype=np.uint8)
for i in range(8):
    r[:,:,i] = cv2.bitwise_and(img,x[:,:,i])
    mask = r[:,:,i]>0
    r[mask] = 255
    cv2.imshow(str(i),r[:,:,i])
cv2.waitKey()
cv2.destroyAllWindows()



