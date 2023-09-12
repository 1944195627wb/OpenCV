#Hu矩函数
#hu = cv2.HuMoments(m)
#ho =nu20+nu02
import cv2
o1 = cv2.imread("D:/photo/wen.webp",0)
HuM1 = cv2.HuMoments(cv2.moments(o1)).flatten()
print("cv2.moments(o1)=\n",cv2.moments(o1))
print("\nHuM1=\n",HuM1)
print("\ncv2.moments(o1)['nu20']+cv2.moments(o1)['nu20']=\n",cv2.moments(o1)['nu20']+cv2.moments(o1)['nu02'])
print("HuM1[0]=",HuM1[0])
print("\nHu[0]-(nu02+nu20)=",HuM1[0]-(cv2.moments(o1)['nu20']+cv2.moments(o1)['nu02']))
