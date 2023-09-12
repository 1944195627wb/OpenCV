#shape属性的第一个是行fy(外层数量)，第二个属性是列fx(内层数量)
import cv2
img = cv2.imread("D:/photo/1.png")
rst = cv2.resize(img,None,fx=2,fy=0.5)
print("img.shape=",img.shape)
print("rst.shape=",rst.shape)