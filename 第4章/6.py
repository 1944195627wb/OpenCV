#HSV
#H[0,360]S[0,1]V[0,1]
#分析得到肤色的HSV值，就可以直接在图像内根据肤色的HSV值来查找人脸（等皮肤）区域。

import cv2
import numpy as np
imgBlue = np.zeros([1,1,3],dtype=np.uint8)
imgBlue[0,0,0] = 255
Blue = imgBlue
BlueHSV = cv2.cvtColor(Blue,cv2.COLOR_BGR2HSV)
print("Blue=\n",Blue)
print("BlueHSV=\n",BlueHSV)

imgGreen =np.zeros([1,1,3],dtype=np.uint8)
imgGreen[0,0,1]=255
Green = imgGreen
GreenHSV = cv2.cvtColor(Green,cv2.COLOR_BGR2HSV)
print("Green=\n",Green)
print("GreenHSV=\n",GreenHSV)

imgRed=np.zeros([1,1,3],dtype=np.uint8)
imgRed[0,0,2] =255
Red=imgRed
RedHSV =cv2.cvtColor(Red,cv2.COLOR_BGR2HSV)
print("Red=\n",Red)
print("RedHSV=\n",RedHSV)