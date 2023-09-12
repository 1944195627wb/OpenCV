#通道合并——cv2.merge([b,g,r])
import cv2
img = cv2.imread("D:/photo/1.png")
b,g,r = cv2.split(img)
bgr = cv2.merge([b,g,r])
rgb = cv2.merge([r,g,b])
brg = cv2.merge([b,r,g])
cv2.imshow("img",img)
cv2.imshow("bgr",bgr)
cv2.imshow("rgb",rgb)
cv2.imshow("brg",brg)
cv2.waitKey()
cv2.destroyAllWindows()
