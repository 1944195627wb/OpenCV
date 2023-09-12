import cv2
o = cv2.imread("D:/photo/16.jpg")
r = cv2.boxFilter(o,-1,(5,5),normalize=0)
cv2.imshow("original",o)
cv2.imshow("result",r)
cv2.waitKey()
cv2.destroyAllWindows()