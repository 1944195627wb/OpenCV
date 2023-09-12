import cv2
o = cv2.imread("D:/photo/hand.png",0)
cv2.imshow("original",o)
ret,binary = cv2.threshold(o,127,255,cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
hull = cv2.convexHull(contours[0])
o = cv2.polylines(o,[hull],True,(255,255,0),1)

distA = cv2.pointPolygonTest(hull,(200,150),False)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(o,'A',(200,150),font,1,(255,255,0),3)
print("distA =",distA)

distB = cv2.pointPolygonTest(hull,(100,150),False)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(o,'B',(100,150),font,1,(0,255,0),3)
print("distB=",distB)

distC = cv2.pointPolygonTest(hull,(100,180),False)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(o,'C',(100,180),font,1,(0,0,255),3)
print("distC=",distC)

cv2.imshow("result",o)
cv2.waitKey()
cv2.destroyAllWindows()