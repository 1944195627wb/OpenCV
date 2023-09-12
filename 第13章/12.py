#pyplot模块介绍
#subplot函数
#matplotlib.pyplot.subplot(nrows,ncols,index)
import cv2
import matplotlib.pyplot as plt
img = cv2.imread("D:/photo/5.jpg",0)
equ = cv2.equalizeHist(img)
plt.figure("subplot示例")
plt.subplot(121),plt.hist(img.ravel(),256)
plt.subplot(122),plt.hist(equ.ravel(),256)
plt.show()