import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread("D:/photo/1.png")
data=img.reshape((-1,3))
data=np.float32(data)
criteria=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER)
ret,label,center=cv2.kmeans(data,2,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
center=np.uint8(center)
res1=center[label.flatten()]
res2=res1.reshape((img.shape))
plt.subplot(121)
plt.imshow(img)
plt.axis('off')
plt.subplot(122)
plt.imshow()