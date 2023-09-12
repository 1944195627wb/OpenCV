import cv2
import matplotlib.pyplot as plt
o = cv2.imread("D:/photo/5.jpg",0)
hist = cv2.calcHist([o],[0],None,[256],[0,255])
plt.plot(hist,color='b')
plt.show()