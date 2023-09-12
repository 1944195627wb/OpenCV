#释放指定窗口--None = cv2.destroyWindow(winname)
import cv2
img = cv2.imread("D:/photo/1.png")
cv2.imshow("img",img)
cv2.waitKey()
cv2.destroyWindow("img")