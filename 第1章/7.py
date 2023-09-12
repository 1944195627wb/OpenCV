#保存图像 -- retval = cv2.imwrite(filename,img[,params])
import cv2
img = cv2.imread("D:/photo/1.png")
r = cv2.imwrite("D:/photo/1.jpg",img)