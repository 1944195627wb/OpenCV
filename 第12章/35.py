#idx = cv2.findNonzero(src)
import cv2
import numpy as np
a = np.random.randint(0,2,size=[5,5],dtype=np.uint8)
print("a=\n",a)
loc = cv2.findNonZero(a)
print("a内非零值的位置：\n",loc)
