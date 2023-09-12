#锁定特定值
#dst =cv2.inRange(src,lowerb,upperb)
import cv2
import numpy as np
img = np.random.randint(0,256,size=[5,5],dtype=np.uint8)
_min = 100
_max = 200
mask = cv2.inRange(img,_min,_max)
print("img=\n",img)
print("mask=\n",mask)
