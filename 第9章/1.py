#图像梯度——计算图像的边缘信息——通过计算像素值的差得到梯度的近似值
#Sobel理论基础
#如果要计算像素点P5的水平方向偏导数P5x，则需要利用Sobel算子及P5邻域点，所使用的公式为：
#P5x=（P3-P1）+2·（P6-P4）+（P9-P7）右-左
# 如果要计算像素点P5的垂直方向偏导数P5y，则需要利用Sobel算子及P5邻域点，所使用的公式为：
# P5y=（P7-P1）+2·（P8-P2）+（P9-P3）下-上
#dst = cv2.Sobel(src,ddepth,dx,dy[,ksize[,scale[,delta[,borderType]]]])
#为了防止信息丢失，通常要将函数cv2.Sobel（）内参数ddepth的值设置为“cv2.CV_64F”
#P5Sobel=|P5x|+|P5y|=|（P3-P1）+2·（P6-P4）+（P9-P7）|+|（P7-P1）+2·（P8-P2）+（P9-P3）|
#对参数取绝对值——dst = cv2.convertScaleAbs(src[,alpha[,beta]])
# dst = saturate(src*alpha+beta)
import cv2
import numpy as np
img = np.random.randint(-256,256,size=[4,5],dtype=np.int16)
rst = cv2.convertScaleAbs(img)
print("img=\n",img)
print("rst=\n",rst)

