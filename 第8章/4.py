#膨胀——腐蚀的逆操作——将与当前对象（前景）接触到的背景点合并到当前对象内，从而实现将图像的边界点向外扩张
# dst = cv2.dilate(src,kernel[,anchor[,iterations[borderType[,borderValue])
# import cv2
# import numpy as np
# img = np.zeros((5,5),np.uint8)
# img[2,1:4] = 1
# kernel = np.ones((3,1),np.uin8)
# dilation = cv2.dilate(img,kernel)
# print("img=\n",img)
# print("kernel=\n",kernel)
# print("diltion=\n",dilation)

import cv2
import numpy as np
o = cv2.imread("D:/photo/R.png")
kernel = np.ones((9,9),np.uint8)
dilation = cv2.dilate(o,kernel)
cv2.imshow("original",o)
cv2.imshow("dilation",dilation)
cv2.waitKey()
cv2.destroyAllWindows()