#生成仿射函数所使用的转化矩阵
#retval=cv2.getAffineTransform(src,dst)
import cv2
import numpy as np
img = cv2.imread("D:/photo/1.png")
rows,cols,ch = img.shape#先行再列
p1 = np.float32([[0,0],[cols-1,0],[0,rows-1]])#先列再行
p2 = np.float32([[0,rows*0.33],[cols*0.85,rows*0.25],[cols*0.15,rows*0.7]])
M = cv2.getAffineTransform(p1,p2)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow("origianl",img)
cv2.imshow("result",dst)
cv2.waitKey()
cv2.destroyAllWindows()
