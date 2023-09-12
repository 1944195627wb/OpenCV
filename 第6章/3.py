#反二值化阈值处理->cv2.THRESH_BINARY_INV
#dst(x,y) =0(src(x,y)>thresh/=maxxval(其他情况)
import cv2
import numpy as np
img = np.random.randint(0,256,size=[4,5],dtype=np.uint8)
t,rst = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
print("img=\n",img)
print("t=\n",t)
print("rst=\n",rst)
