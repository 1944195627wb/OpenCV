#加权和
#二者相同
#cv2.addWeighted(src1,alpha,src2,beta,gamma)
#图像=图像1x系数1+图像2x系数2+亮度调节量(必选参数)
import cv2
import numpy as np
img1 = np.ones((3,4),dtype=np.uint8)*100
img2 = np.ones((3,4),dtype=np.uint8)*10
gamma = 3
img3 = cv2.addWeighted(img1,0.6,img2,5,gamma)
print(img3)

