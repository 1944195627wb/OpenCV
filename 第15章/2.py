import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("D:/photo/5.jpg",0)
template =img[200:400,200:400]
tw,th = template.shape[::-1]
rv = cv2.matchTemplate(img,template,cv2.TM_CCOEFF)
minVal,maxVal,minLoc,maxLoc = cv2.minMaxLoc(rv)
topLeft = maxLoc
bottomRight = (topLeft[0]+tw,topLeft[1]+th)
cv2.rectangle(img,topLeft,bottomRight,255,2)
plt.subplot(121),plt.imshow(rv,cmap='gray')
plt.title('Matching Result'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(img,cmap='gray')
plt.title('Detected Point'),plt.xticks([]),plt.yticks([])
plt.show()
