#矩特征
#retval = cv2.moments(array[,binaryImage])
import cv2
import numpy as np
o = cv2.imread("D:/photo/wen.webp")
cv2.imshow("original",o)
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
ret,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
n = len(contours)
contours_img = []
for i in range(n):
    temp = np.zeros(o.shape,np.uint8)
    contours_img.append(temp)
    contours_img[i] = cv2.drawContours(contours_img[i],contours,i,(255,255,0),-1,8,hierarchy=hierarchy)
    cv2.imshow("contours["+str(i)+"]",contours_img[i])
print("观察各个轮廓的矩(moments):")
for i in range(n):
    print("轮廓"+str(i)+"的矩：\n",cv2.moments(contours[i]))
print("观察各个轮廓的面积：")
for i in range(n):
    print("轮廓"+str(i)+"的面积:",cv2.moments(contours[i])["m00"])
cv2.waitKey()
cv2.destroyAllWindows()
