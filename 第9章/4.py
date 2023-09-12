import cv2
o = cv2.imread("D:/photo/cat2.webp")
Sobely = cv2.Sobel(o,cv2.CV_64F,0,1)
Sobely = cv2.convertScaleAbs(Sobely)
cv2.imshow("original",o)
cv2.imshow("y",Sobely)
cv2.waitKey()
cv2.destroyAllWindows()