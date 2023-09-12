#超阈值零处理cv2.THRESH_TOZERO_INV
#dst(x,y) = 0(src(x,y)>thresh/= src(x,y) (其他情况)
import cv2
import numpy as np
img = np.random.randint(0,256,size=[4,5],dtype=np.uint8)
t,rst = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
print("img=\n",img)
print("t",t)
print("rst=\n",rst)