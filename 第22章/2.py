import numpy as np
import cv2
import matplotlib.pyplot as plt
xiaomi=np.random.randint(0,20,(30,2))
dami = np.random.randint(40,60,(30,2))
mi=np.vstack((xiaomi,dami))
mi = np.float32(mi)
criteria=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,10,1.0)
ret,label,center=cv2.kmeans(mi,2,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
print(ret)
print(label)
print(center)
xm = mi[label.ravel()==0]
dm=mi[label.ravel()==1]
plt.scatter(xm[:,0],xm[:,1],c='g',marker='s')
plt.scatter(dm[:,0],dm[:,1],c='r',marker='o')
plt.scatter(center[0,0],center[0,1],s=200,c='b',marker='s')
plt.scatter(center[1,0],center[1,1],s=200,c='b',marker='o')
plt.xlabel('height'),plt.ylabel('width')
plt.show()
