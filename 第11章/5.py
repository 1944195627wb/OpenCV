#拉普拉斯金字塔
#Li=Gi-pyrUp（Gi+1）
import cv2
o = cv2.imread("D:/photo/1.png",0)
p0 = o
p1 = cv2.pyrDown(p0)
p2 = cv2.pyrDown(p1)
p3 = cv2.pyrDown(p2)
l1 = p0 - cv2.pyrUp(p1)
l2 = p1 - cv2.pyrUp(p2)
l3 = p2 - cv2.pyrUp(p3)
print("l1.shape=",l1.shape)
print("l2.shape=",l2.shape)
print("l3.shape=",l3.shape)
cv2.imshow("l1",l1)
cv2.imshow("l2",l2)
cv2.imshow("l3",l3)
cv2.waitKey()
cv2.destroyAllWindows()