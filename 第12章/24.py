#点到轮廓的距离
#retval = cv2.pointPolygonTest(contour,pt,measureDist)
#当值为True时，表示计算点到轮廓的距离。如果点在轮廓的外部，返回值为负数；如果点在轮廓上，返回值为0；如果点在轮廓内部，返回值为正数。
#当值为False时，不计算距离，只返回“-1”、“0”和“1”中的一个值，表示点相对于轮廓的位置关系。如果点在轮廓的外部，返回值为“-1”；如果点在轮廓上，返回值为“0”；如果点在轮廓内部，返回值为“1”。
import cv2
o = cv2.imread("D:/photo/hand.png",0)
cv2.imshow("original",o)
ret,binary = cv2.threshold(o,127,255,cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
hull = cv2.convexHull(contours[0])
o = cv2.polylines(o,[hull],True,(255,255,0),1)

distA = cv2.pointPolygonTest(hull,(200,150),True)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(o,'A',(200,150),font,1,(255,255,0),3)
print("distA =",distA)

distB = cv2.pointPolygonTest(hull,(100,150),True)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(o,'B',(100,150),font,1,(0,255,0),3)
print("distB=",distB)

distC = cv2.pointPolygonTest(hull,(100,180),True)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(o,'C',(100,180),font,1,(0,0,255),3)
print("distC=",distC)

cv2.imshow("result",o)
cv2.waitKey()
cv2.destroyAllWindows()