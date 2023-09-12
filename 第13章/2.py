import cv2
import matplotlib.pyplot as plt
o = cv2.imread("D:/photo/5.jpg")
plt.hist(o.ravel(),16)
plt.show()