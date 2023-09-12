#阈值处理
#1.retval,dst = cv2.threshold(src,thresh,maxval,type)
#二值化阈值处理cv2.THRESH_BINARY
#dst(x,y)=maxval(src(x,y)>thresh) /=0 (其他情况)
import cv2
import numpy as np
img = np.random.randint(0,256,size=[4,5],dtype=np.uint8)
t,rst = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
print("img=\n",img)
print("t",t)
print("rst=\n",rst)

