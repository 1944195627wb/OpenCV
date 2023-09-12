#形态学操作
#腐蚀——能够将图像的边界点消除，使图像沿着边界向内收缩，也可以将小于指定结构体元素的部分去除
#通常使用一个结构元来逐个像素地扫描要被腐蚀的图像，并根据结构元和被腐蚀图像的关系来确定腐蚀结果
# ● 如果结构元完全处于前景图像中（图8-3的左图），就将结构元中
# 心点所对应的腐蚀结果图像中的像素点处理为前景色（白色，像素点的
# 像素值为1）。
# ● 如果结构元未完全处于前景图像中（可能部分在，也可能完全不
# 在，图8-3的右图），就将结构元中心点对应的腐蚀结果图像中的像素
# 点处理为背景色（黑色，像素点的像素值为0）。
# dst = cv2.erode(src,kernel[,anchor[,anchor[,iterations[,borderType[,borderValue])
#kernel 代表腐蚀操作时所采用的结构类型。它可以自定义生成，也可以通过函数cv2.getStructuringElement（）生成。
import cv2
import numpy as np
img = np.zeros((5,5),np.uint8)
img[1:4,1:4] = 1
kernel = np.ones((3,1),np.uint8)
erosion = cv2.erode(img,kernel)
print("img=\n",img)
print("kernel=\n",kernel)
print("erosion=\n",erosion)