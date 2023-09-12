#自适应阈值处理
#dst =dst=cv.adaptiveThreshold（src,maxValue,cv.adaptiveThreshold(src,maxValue,adaptiveMethod,thresholdType,blockSize,C)
#  cv2.ADAPTIVE_THRESH_MEAN_C：邻域所有像素点的权重值是一致的。
#  cv2.ADAPTIVE_THRESH_GAUSSIAN_C：与邻域各个像素点到中心点的距离有关，通过高斯方程得到各个点的权重值。
import cv2
img = cv2.imread("D:/photo/5.jpg",0)
t1,thd = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
athdMEAN = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,3)
athdGAUS = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,3)
cv2.imshow("img",img)
cv2.imshow("thd",thd)
cv2.imshow("athdMEAN",athdMEAN)
cv2.imshow("athdGAUS",athdGAUS)
cv2.waitKey()
cv2.destroyAllWindows()

