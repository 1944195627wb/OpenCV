import cv2
import numpy as np
bule = np.zeros((300,300,3),dtype=np.uint8)
bule[:,:,0]=255
print("bule=\n",bule)
cv2.imshow("bule",bule)
green=np.zeros((300,300,3),dtype=np.uint8)
green[:,:,1]=255
print("green=\n",green)
cv2.imshow("green",green)
red=np.zeros((300,300,3),dtype=np.uint8)
red[:,:,2]=255
print("red=\n",red)
cv2.imshow("red",red)
cv2.waitKey()
cv2.destorAllWindows()
