#模块匹配
#result = cv2.matchTemplate(image,templ,method[mask])
#必须为8位或者32位的浮点型图像
#method:0:方差
#1:平方差匹配
#2:相乘
#3:标准(归一化)相关匹配
#4.均值的相对值
#5:标准(归一化)相关系数匹配
#比较(W-w+1)*(H-h+1)次
#method的值为cv2.TM_SQDIFF和cv2.TM_SQDIFF_NORMED时，result值为0表示匹配度最好，值越大，表示匹配度越差。
#method 的值为 cv2.TM_CCORR、cv2.TM_CCORR_NORMED、cv2.TM_CCOEFF 和cv2.TM_CCOEFF_NORMED时，result的值越小表示匹配度越差，值越大表示匹配度越好。
#minVal,maxVal,minLoc,maxLoc = cv2.minMaxLoc(src[,mask])
#查找最大值或者最小值所在位置
#Img = cv2.rectangle(img,topLeft,bottomRight,color[,thickness])
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("D:/photo/1.png",0)
template = img[400:500,400:500]
th,tw = template.shape[:2]
rv = cv2.matchTemplate(img,template,cv2.TM_SQDIFF)
minVal,maxVal,minLoc,maxLoc=cv2.minMaxLoc(rv)
topLeft = minLoc
bottomRight = (topLeft[0]+tw,topLeft[1]+th)
cv2.rectangle(img,topLeft,bottomRight,255,2)
plt.subplot(121),plt.imshow(rv,cmap='gray')
plt.title("Matching Result"),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(img,cmap='gray')
plt.title('Detected Point'),plt.xticks([]),plt.yticks([])
plt.show()


