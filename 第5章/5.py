#仿射
#cv2.warpAffine()
#dst(x,y) = src(M11x+M12y+M13,M21x+M22y+M23)
#dst=cv2.warpAffine（src,M,dsize[,flags[,borderMode[,borderValue]]]）
#向右为+，向下为+
#M第一个参数是行，第二个参数为列
#平行
import cv2
import numpy as np
img = cv2.imread("D:/photo/1.png")
height,width = img.shape[:2]
x = 100
y = 200
M = np.float32([[1,0,x],[0,1,y]])
move = cv2.warpAffine(img,M,(width,height))
cv2.imshow("original",img)
cv2.imshow("move",move)
cv2.waitKey()
cv2.destroyAllWindows()