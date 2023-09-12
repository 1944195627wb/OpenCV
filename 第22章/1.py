#K均值聚类
# 1.随机选取k个点作为分类的中心点。
# 2.将每个数据点放到距离它最近的中心点所在的类中。
# 3.重新计算各个分类的数据点的平均值，将该平均值作为新的分类中心点。
# 4.重复步骤2和步骤3，直到分类稳定。
#retval,bestLabels,centers=cv2.kmeans（data,K,bestLabels,criteria,attempts,flags）
import numpy as np
import cv2
from matplotlib import pyplot as plt
xiaomi = np.random.randint(0,50,60)
dami = np.random.randint(200,250,60)
mi = np.hstack((xiaomi,dami))
mi = mi.reshape(120,1)
mi=np.float32(mi)
criteria=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,10,1.0)
flags=cv2.KMEANS_RANDOM_CENTERS
retval,bestLabels,centers=cv2.kmeans(mi,2,None,criteria,10,flags)
print(retval)
print(bestLabels)
print(centers)
xm=mi[bestLabels==0]
dm=mi[bestLabels==1]
plt.plot(xm,'ro')
plt.plot(dm,'bo')
plt.plot(centers[0],'rx')
plt.plot(centers[1],'bx')
plt.show()