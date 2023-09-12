#人脸数据库
#1.CAS-PEAL
#2.AT&T Facedatabase
#3.Yale Facedatabase A
#4.Extended Yale Facedatabase B
#5.color FERET Database
import cv2
img=cv2.imread("D:/photo/touxiang.jpg")
b,g,r=cv2.split(img)
rgb=cv2.merge([r,g,b])
rbg=cv2.merge([r,b,g])
bgr=cv2.merge([b,g,r])
brg=cv2.merge([b,r,g])
gbr=cv2.merge([g,b,r])
grb=cv2.merge([g,r,b])
cv2.imshow("rgb",rgb)
cv2.imshow("rbg",rbg)
cv2.imshow("bgr",bgr)
cv2.imshow("brg",brg)
cv2.imshow("gbr",gbr)
cv2.imshow("grb",grb)
cv2.imwrite("D:/photo/rgb.jpg",rgb)
cv2.waitKey()

