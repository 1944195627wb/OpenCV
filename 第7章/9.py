import cv2
o = cv2.imread("D:/photo/1.png")
g = cv2.GaussianBlur(o,(55,55),0,0)
b = cv2.bilateralFilter(o,25,100,100)
cv2.imshow("original",o)
cv2.imshow("Gaussian",g)
cv2.imshow("bilateral",b)
cv2.waitKey()
cv2.destroyAllWindows()