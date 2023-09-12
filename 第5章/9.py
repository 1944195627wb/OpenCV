#重映射
#dst=cv2.remap（src,map1,map2,interpolation[,borderMode[,borderValue]]）
# ● map1参数有两种可能的值：
# ● 表示（x,y）点的一个映射。
# ● 表示CV_16SC2 ,CV_32FC1,CV_32FC2类型（x,y）点的x值。
# ● map2参数同样有两种可能的值：
# ● 当map1表示（x,y）时，该值为空。
# ● 当map1表示（x,y）点的x值时，该值是CV_16UC1,CV_32FC1类型（x,y）点的y值。
import cv2
import numpy as np
img = np.random.randint(0,256,size=[4,5],dtype=np.uint8)
rows,cols=img.shape
map1 = np.ones(img.shape,np.float32)*3#列
map2 = np.ones(img.shape,np.float32)*0#行
rst = cv2.remap(img,map1,map2,cv2.INTER_LINEAR)
print("img=\n",img)
print("map1=\n",map1)
print("map2=\n",map2)
print("rst=\n",rst)