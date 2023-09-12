#绘图及交互
#绘画基础
#1.绘制直线
#img = cv2.line(img,pt1,pt2,color[,thickness[,lineType]])
import numpy as np
import cv2
n = 300
img = np.zeros((n+1,n+1,3),np.uint8)
img = cv2.line(img,(0,0),(n,n),(255,0,0),3)
img = cv2.line(img,(0,100),(n,100),(0,255,0),1)
img = cv2.line(img,(100,0),(100,n),(0,0,255),6)
win_name='Demo19.1'
cv2.imshow(win_name,img)
cv2.waitKey()
cv2.destroyAllWindows()