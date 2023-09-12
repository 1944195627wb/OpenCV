import cv2
import numpy as np
o = cv2.imread("D:/photo/1.png")
g0 = o
g1 = cv2.pyrDown(g0)
g2 = cv2.pyrDown(g1)
g3 = cv2.pyrDown(g2)
l0 = g0 - cv2.pyrUp(g1)
l1 = g1 - cv2.pyrUp(g2)
l2 = g2 - cv2.pyrUp(g3)
rg0 = l0 + cv2.pyrUp(g1)
print("g0.shape",g0.shape)
print("rg0.shape",rg0.shape)
result = rg0-g0
result = abs(result)
print(np.sum(result))
rg1 = l1 + cv2.pyrUp(g2)
print("g1.shape",g1.shape)
print("rg1.shape",rg1.shape)
result =rg1-g1
result =abs(result)
print(np.sum(result))
rg2 = l2 +cv2.pyrUp(g3)
print("g2.shape",g2.shape)
print("rg2.shape",rg2.shape)
result =rg2 -g2
result =abs(result)
print(np.sum(result))