#通过函数拆分
#b,g,r=cv2.split(img)
#<=>b=cv2.split(img)[0]
#   g=cv2.split(img)[1]
#   r=cv2.split(img)[2]
import cv2
img = cv2.imread("D:/photo/1.png")
b,g,r=cv2.split(img)
cv2.imshow("B",b)
cv2.imshow("G",g)
cv2.imshow("R",r)
cv2.waitKey()
cv2.destoryAllWindows()