#透视
#dst = cv2.warpPerspective(src,M,dsize[,flags[,borderMode[,borderValue])
#变换矩阵：retval = cv2.getPerspectiveTransform(src,dst)
import cv2
import numpy as np
img = cv2.imread("D:/photo/1.png")
rows,cols=img.shape[:2]
print(rows,cols)
pts1 = np.float32([[150,50],[400,50],[60,450],[310,450]])
pts2 = np.float32([[50,50],[rows-50,50],[50,cols-50],[rows-50,cols-50]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(cols,rows))
cv2.imshow("img",img)
cv2.imshow("dst",dst)
cv2.waitKey()
cv2.destroyAllWinows()