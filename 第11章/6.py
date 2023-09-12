#使用拉普拉斯金字塔恢复
import cv2
import numpy as np
o = cv2.imread("D:/photo/1.png")
G0 = o
G1 = cv2.pyrDown(G0)
L0 = G0 - cv2.pyrUp(G1)
R0 = L0+cv2.pyrUp(G1)
print("o.shape",o.shape)
print("RO.shape",R0.shape)
result = R0 - o
result = abs(result)
print(np.sum(result))