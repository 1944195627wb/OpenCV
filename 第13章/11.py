#直方图均衡化
#dst = cv2.equalizeHist(src)
import cv2
import matplotlib.pyplot as plt
img = cv2.imread("D:/photo/5.jpg",0)
equ =cv2.equalizeHist(img)
cv2.imshow("original",img)
cv2.imshow("result",equ)
plt.figure("原始图像直方图")
plt.hist(img.ravel(),256)
plt.figure("均衡化结果直方图")
plt.hist(equ.ravel(),256)
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()