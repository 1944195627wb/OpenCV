#x，y轴互换
import  cv2
import numpy as np
img = np.random.randint(0,256,size=[4,6],dtype=np.uint8)
rows,cols = img.shape
map1 = np.zeros(img.shape,np.float32)
map2 = np.zeros(img.shape,np.float32)
for i in range(rows):
    for j in range(cols):
        map1.itemset((i,j),i)
        map2.itemset((i,j),j)
rst = cv2.remap(img,map1,map2,cv2.INTER_LINEAR)
print("img=\n",img)
print("map1=\n",map1)
print("map2=\n",map2)
print("rst=\n",rst)
