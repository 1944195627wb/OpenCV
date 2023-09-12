import cv2
img = cv2.imread("D:/photo/1.png")
rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow("img",img)
cv2.imshow("bgr",rgb)
cv2.waitKey()
cv2.destroyAllWindows()