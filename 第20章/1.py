#K近邻算法
#理论基础
import cv2
import numpy as np
import matplotlib.pyplot as plt
s = 'image\\'
num = 100
row =240
col = 240
a = np.zeros((num,row,col))
print(a.shape)
print(a.shape)
n = 0
for i in range(0,10):
    for j in range(1,11):
        a[n,:,:] = cv2.imread(s+str(i)+'\\'+str(i)+'-'+str(j)+'.bmp',0)
        n = n+1
feature = np.zeros((num,round(row/5),round(col/5)))
print(feature.shape)
print(row)
for ni in range(0,num):
    for nr in range(0,row):
        for nc in range(0,col):
            if a[ni,nr,nc]==255:
                feature[ni,int(nr/5),int(nc/5)]+=1
f = feature
o = cv2.imread('image\\test\\5.bmp',0)
of = np.zeros((round(row/5),round(col/5)))
for nr in range(0,row):
    for nc in range(0,col):
        if o[nr,nc]==255:
            of[int(nr/5),int(nc/5)]+=1
d = np.zeros(100)
for i in range(0,100):
    d[i]=np.sum((of-f[i,:,:])*(of-f[i,:,:]))
print(d)
d = d.tolist()
temp=[]
inf = max(d)
print(inf)
k=7
for i in range(k):
    temp.append(d.index(min(d)))
    d[d.index(min(d))]=inf
print(temp)
temp = [i/10 for i in temp]
temp = np.array(temp)
temp = np.trunc(temp/10)
print(temp)
r = np.zeros(10)
for i in temp:
    r[int(i)]+=1
print(r)
print('当前的数字可能为'+str(np.argmax(r)))
