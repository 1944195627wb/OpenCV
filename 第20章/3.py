import cv2
import numpy as np
import matplotlib.pyplot as plt
s = 'image\\'
num = 100
row =240
col=240
a=np.zeros((num,row,col))
print(a.shape)
n=0
for i in range(0,10):
    for j in range(1,11):
        a[n,:,:] = cv2.imread(s+str(i)+'\\'+str(i)+'-'+str(j)+'.bmp',0)
feature = np.zeros((num,round(row/5),round(col/5)))
print(feature.shape)
print(row)
for ni in range(0,num):
    for nr in range(0,row):
        for nc in range(0,col):
            if a[ni,nr,nc]==255:
                feature[ni,int(nr/5),int(nc/5)]+=1
f = feature
train = feature[:,:].reshape(-1,round(row/5)*round(col/5)).astype(np.float32)
print(train.shape)
trainLabels = [int(i)/10 for i in range(0,100)]
trainLabels=np.asarray(trainLabels)
print(*trainLabels)
o = cv2.imread('image\\test\\5.bmp',0)
of =np.zeros((round(row/5),round(col/5)))
for nr in range(0,row):
    for nc in range(0,col):
        if o[nr,nc]==255:
            of[int(nr/5),int(nc/5)]+=1
test = of.reshape(-1,round(row/5)*round(col/5)).astype(np.float32)
knn = cv2.ml.KNearest_create()
knn.train(train,cv2.ml.ROW_SAMPLE,trainLabels)
ret,result,neighbours,dist = knn.findNearest(test,k=5)
print("当前随机数可以判定为类型：",result)
print("距离当前点最进的5个邻居是",neighbours)
print("5个最近邻居的距离;",dist)
