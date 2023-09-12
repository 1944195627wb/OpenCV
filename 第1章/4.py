import cv2
img = cv2.imread("D:/photo/1.png")
cv2.imshow("img",img)
key = cv2.waitKey()
if key !=-1:
    print("触发了按键")