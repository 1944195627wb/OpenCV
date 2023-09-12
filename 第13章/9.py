#使用掩模绘制直方图
import cv2
import numpy as np
mask = np.zeros([960,960],np.uint8)
mask[200:400,200:400] = 255
cv2.imshow("mask",mask)
cv2.waitKey()
cv2.destroyAllWindows()