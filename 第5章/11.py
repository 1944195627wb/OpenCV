import cv2
import numpy as np
img = cv2.imread("D:/photo/1.png")
rows,cols= img.shape[:2]
map1 = np.zeros(img.shape[:2],np.float32)
map2 = np.zeros(img.shape[:2],np.float32)
for i in range(rows):
    for j in range(cols):
        map1.itemset((i,j),j)
        map2.itemset((i,j),i)
rst = cv2.remap(img,map1,map2,cv2.INTER_LINEAR)
cv2.imshow("original",img)
cv2.imshow("result",rst)
cv2.waitKey()
cv2.destroyAllWindows()