#掩模和像素点
import numpy as np
a = np.random.randint(0,2,size=[5,5],dtype=np.uint8)
print("a=\n",a)
loc = np.transpose(np.nonzero(a))
print("a内非0值的位置信息\n",loc)
