#缩放
import cv2
import numpy as np
img = cv2.imread("D:/photo/1.png")
rows,cols= img.shape[:2]
map1 = np.zeros(img.shape[:2],np.float32)
map2 = np.zeros(img.shape[:2],np.float32)
for i in range(rows):
    for j in range(cols):
        if 0.25*cols < i < 0.75*cols and 0.25*rows <j <0.75*rows:
            map1.itemset((i,j),2*(j-cols*0.25)+0.5)
            map2.itemset((i,j),2*(i-rows*0.25)+0.5)
        else:
            map1.itemset((i,j),0)
            map2.itemset((i,j),0)
rst = cv2.remap(img,map1,map2,cv2.INTER_LINEAR)
print(map1)
print(map2)
cv2.imshow("original",img)
cv2.imshow("result",rst)
cv2.waitKey()
cv2.destroyAllWindows()