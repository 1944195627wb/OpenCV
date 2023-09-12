#多模块匹配
#函数where（）能够获取模板匹配位置的集合
#函数zip（）用可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
#loc[::-1]——行列进行互换
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("D:/photo/5.jpg",0)
template = img[200:400,200:400]
w,h = template.shape[::-1]
res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where(res>=threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),255,1)
plt.imshow(img,cmap='gray')
plt.xticks([]),plt.yticks([])
plt.show()