#通过索引拆分
#b=img[:,:,0]
#g=img[:,:,1]
#r=img[:,:,2]
import cv2
img = cv2.imread("D:/photo/1.png")
cv2.imshow("img",img)
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]
cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)
img[:,:,0]=0
cv2.imshow("img0",img)
img[:,:,1]=0
cv2.imshow("img1",img)
cv2.waitKey()
cv2.destoryAllWindows()