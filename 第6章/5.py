#截断阈值化处理cv2.THRESH_TRUNC
#dst(x,y)=thresh((src(x,y)>thresh)/=0(其他情况)
import cv2
import numpy as np
img = np.random.randint(0,256,size=[4,5],dtype=np.uint8)
t,rst = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
print("img=\n",img)
print("t",t)
print("rst=\n",rst)
