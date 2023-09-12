#计算轮廓的长度：arcLength函数
#retval=cv2.arcLength(curve,closed)
import cv2
import numpy as np
o = cv2.imread("D:/photo/wen.webp",0)
ret,binary = cv2.threshold(o,17,155,cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
n = len(contours)
cntLen = []
for i in range(n):
    cntLen.append(cv2.arcLength(contours[i],True))
    print("第["+str(i)+"]个轮廓的长度为:",cntLen[i])
    cntLenSum = np.sum(cntLen)
    cntLenAvr = cntLenSum/n
    print("轮廓的总长度为:",cntLenSum)
    print("轮廓的平均长度为:",cntLenAvr)
contours_img=[]
for i in range(n):
    temp = np.zeros(o.shape,np.uint8)
    contours_img.append(temp)
    contours_img[i]=cv2.drawContours(contours_img[i],contours,i,(255,255,0),3)
    if cv2.arcLength(contours[i],True)>cntLenAvr:
        cv2.imshow("contours["+str(i)+"]",contours_img[i])
cv2.waitKey()
cv2.destroyAllWindows()