#色彩空间类型转换
#RGB -> GRAY
#Gray = 0.299*R+0.587*G+0.114*B  或者 Gray =(R+G+B)/3

#GRAY -> RGB
#R = Gray G=Gray B=Gray

#RGB -> YCrCb
#Y = 0.299*R+0.587*G+0.114*B
#Cr = (R-Y)*0.713+delta
#Cb = (B-Y)*0.564+delta

#delta=128(8位)/=32768(16位)/=0.5(单精度)

#YCrCb -> RGB
#R = Y+1.403*(Cr-delta)
#G = Y -0.714*(Cr-delta)-0.344*(Cb -delta)
#B = Y +1.773*(Cb-delta)

#HSV色调 饱和度 亮度
#色调[0,360],0:红色,60:黄色,120:绿色,180:青色,240:蓝色,300:品红色
#饱和度[0,1]0为灰度
##亮度[0,1]
#RGB ->HSV
# V = max(R,G,B)
# S = (V-min(R,G,B))/V (V!=0)
# S=0(其他情况)
# H = (60(G-B))/(V-min(R,G,B))(V=R)
# H = (60(B-R))/(V-min(R,G,B))+120(V=G)
# H = (60(R-B))/(V-min(R,G,B))+240(V=B)
# 若H<0 则H+360

#CIEL*a*b*色彩空间
#L* ：像素的亮度 [0,100] a*：从红色到绿色 [-127,127]b*：从黄色到蓝色[-127,127]
#CIEL*u*v*色彩空间
#L*[0,100] u[-134,220] v[-140,122]
#Bayer色彩空间
#类型转换函数
# dst = cv2.cvtColor(src,code[,dstCn])
#图像类型转化表格 由P166~174
#8位:233,16位:565,24位:888,32位:24+12(透明度)浮点数图像值[0,1]

import cv2
import numpy as np
img = np.random.randint(0,256,size=[2,4,3],dtype=np.uint8)
rst = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print("img=\n",img)
print("rst=\n",rst)
print("像素点(1,0)直接计算得到的值=",img[1,0,0]*0.114+img[1,0,1]*0.587+img[1,0,2]*0.299)
print("像素点(1,0)使用公式cv2.cvtColor()转换值=",rst[1,0])