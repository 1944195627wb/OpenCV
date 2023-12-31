import cv2
o = cv2.imread("D:/photo/hand.png",0)
cv2.imshow("original",o)
ret,binary = cv2.threshold(o,127,255,cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
hull = cv2.convexHull(contours[0])
cv2.polylines(o,[hull],True,(255,255,0),2)
cv2.imshow("result",o)
cv2.waitKey()
cv2.destroyAllWindows()