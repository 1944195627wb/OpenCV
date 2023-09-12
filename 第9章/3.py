import cv2
o = cv2.imread("D:/photo/cat2.webp")
Sobelx = cv2.Sobel(o,cv2.CV_64F,1,0)
Sobelx = cv2.convertScaleAbs(Sobelx)
cv2.imshow("original",o)
cv2.imshow("x",Sobelx)
cv2.waitKey()
cv2.destroyAllWindows()