#旋转
#retval = cv2.getRotationMatrix2D(center（中心点）,angle（角度）,scale（缩放大小）)
#angle正数表示逆时针，负数表示顺时针
import cv2
img = cv2.imread("D:/photo/1.png")
height,width = img.shape[:2]
M =cv2.getRotationMatrix2D((width/2,height/2),45,0.6)
rotate = cv2.warpAffine(img,M,(width,height))
cv2.imshow("original",img)
cv2.imshow("rotation",rotate)
cv2.waitKey()
cv2.destroyAllWindows()