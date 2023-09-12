import cv2
import numpy as np
img = cv2.imread("D:/photo/1.png")
cv2.imshow("before",img)
print("访问img.item(0,0,0)=",img.item(0,0,0))
print("访问img.item(0,0,1)=",img.item(0,0,1))
print("访问img,item(0,0,2)=",img.item(0,0,2))
for i in range(0,50):
    for j in range(0,100):
        for k in range(0,3):
            img.itemset((i,j,k),255)
cv2.imshow("after",img)
cv2.waitKey()
print("修改后img.item(0,0,0)=",img.item(0,0,0))
print("修改后img.item(0,0,1)=",img.item(0,0,1))
print("修改后img,item(0,0,2)=",img.item(0,0,2))