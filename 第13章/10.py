import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread("D:/photo/5.jpg",0)
mask = np.zeros(image.shape,np.uint8)
mask[200:800,200:800] = 255
histImage = cv2.calcHist([image],[0],None,[256],[0,255])
histMI =cv2.calcHist([image],[0],mask,[256],[0,255])
plt.plot(histImage)
plt.plot(histMI)
plt.show()

