import cv2
o = cv2.imread("D:/photo/cat2.webp")
k1 = cv2.getStructuringElement(cv2.MORPH_RECT,(20,20))
k2 = cv2.getStructuringElement(cv2.MORPH_CROSS,(20,20))
k3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(20,20))
r1 = cv2.dilate(o,k1)
r2 = cv2.dilate(o,k2)
r3 = cv2.dilate(o,k3)
cv2.imshow("o",o)
cv2.imshow("r1",r1)
cv2.imshow("r2",r2)
cv2.imshow("r3",r3)
cv2.waitKey()
cv2.destroyAllWindows()