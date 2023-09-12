#直方图处理
#DIMS/RANGE/BINS
#绘制直方图
#1.numpy方法——matplotlib.pyplot.hist(X,BINS)
#b= a.ravel()——降维处理
import cv2
import matplotlib.pyplot as plt
o = cv2.imread("D:/photo/6.webp")
cv2.imshow("original",o)
plt.hist(o.ravel(),256)
cv2.waitKey()
cv2.destroyAllWindows()

