#创建窗口 -- None = cv2.namedWindow(winname)
#显示图像 -- None = cv2.namedWindow(winname,mat)
import cv2
img = cv2.imread("D:/photo/1.png")
cv2.namedWindow("img")
cv2.imshow("img",img)


#import cv2
#img = cv2.imread("D:/photo/1.png")
#cv2.imshow("img",img)

