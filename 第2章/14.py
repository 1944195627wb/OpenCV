import cv2
import numpy as np
img = cv2.imread("D:/photo/1.png")
cv2.imshow("original",img)
nose = np.random.randint(0,256,size=[180,100,3],dtype=np.uint8)
img[220:400,250:350]=nose
cv2.imshow("result",img)
cv2.waitKey()
cv2.destoryAllWindows()