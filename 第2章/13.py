import cv2
img = cv2.imread("D:/photo/1.png",cv2.IMREAD_UNCHANGED)
nose=img[220:400,250:350]
cv2.imshow("original",img)
cv2.imshow("nose",nose)
cv2.waitKey()
cv2.destoryAllWindows()