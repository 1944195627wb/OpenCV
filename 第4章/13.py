import cv2
img = cv2.imread("D:/photo/1.png")
bgra = cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)
b,g,r,a =cv2.split(bgra)
a[:,:]=125
bgra125=cv2.merge([b,g,r,a])
a[:,:]=0
bgra0 =cv2.merge([b,g,r,a])
cv2.imshow("img",img)
cv2.imshow("bgra",bgra)
cv2.imshow("bgra125",bgra125)
cv2.imshow("bgra0",bgra0)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite("D:/photo/bgra.png",bgra)
cv2.imwrite("D:/photo/bgra125.png",bgra125)
cv2.imwrite("D:/photo/bgra0.png",bgra0)