import numpy as np
import cv2
import matplotlib.pyplot as plt
rand1 = np.random.randint(0,30,(20,2)).astype(np.float32)
rand2 = np.random.randint(70,100,(20,2)).astype(np.float32)
trainData = np.vstack((rand1,rand2))
r1Label = np.zeros((20,1)).astype(np.float32)
r2Label = np.ones((20,1)).astype(np.float32)
tdLable = np.vstack((r1Label,r2Label))
g = trainData[tdLable.ravel()==0]
plt.scatter(g[:,0],g[:,1],80,'g','o')
b = trainData[tdLable.ravel()==1]
plt.scatter(b[:,0],b[:,1],80,'b','s')
test = np.random.randint(0,100,(1,2)).astype(np.float32)
plt.scatter(test[:,0],test[:,1],80,'r','*')
knn=cv2.ml.KNearest_create()
knn.train(trainData,cv2.ml.ROW_SAMPLE,tdLable)
ret,results,neighbours,dist=knn.findNearest(test,5)
print("当前随机数可以判定为类型：",results)
print("距离当前点最近的5个邻居是",neighbours)
print("5个最近邻居的距离：",dist)
plt.show()
