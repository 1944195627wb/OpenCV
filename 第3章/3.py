import cv2
a = cv2.imread("D:/photo/1.png",0)
b = a
result1 = a+b
result2 = cv2.add(a,b)
cv2.imshow("original",a)
cv2.imshow("result1",result1)
cv2.imshow("result2",result2)
cv2.waitKey()
cv2.destroyAllWindows()