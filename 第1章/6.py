#释放所有窗口 None = cv2.destroyAllWindows()
import cv2
img = cv2.imread("D:/photo/1.png")
cv2.imshow("img1",img)
cv2.imshow("img2",img)
cv2.waitKey()
cv2.destroyAllWindows()