#Canny边缘检测
#1、应用高斯滤波去除图像噪声
#2、计算梯度
#3、非极大值抑制
#4、应用双阈值确定边缘
# edges=cv.Canny（image,threshold1,threshold2[,apertureSize[,L2gradient]]）
# edges为计算得到的边缘图像。
# image为8位输入图像。
# threshold1表示处理过程中的第一个阈值。
# threshold2表示处理过程中的第二个阈值。
# apertureSize表示Sobel算子的孔径大小。
# L2gradient为计算图像梯度幅度（gradient magnitude）的标识。其默认值为False。如果为 True，则使用更精确的 L2范数进行计算（即两个方向的导数的平方和再开方），否则使用L1范数（直接将两个方向导数的绝对值相加）。
import cv2
o =cv2.imread("D:/photo/5.jpg",0)
r1 = cv2.Canny(o,128,200)
r2 = cv2.Canny(o,32,128)
cv2.imshow("original",o)
cv2.imshow("result1",r1)
cv2.imshow("result2",r2)
cv2.waitKey()
cv2.destroyAllWindows()

