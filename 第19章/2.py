#绘制矩形
#img = cv2.rectangle(img,pt1,pt2,color[,thickness[,lineType]])
import numpy as np
import cv2
n = 300
img = np.ones((n,n,3),np.uint8)*255
img = cv2.rectangle(img,(50,50),(n-100,n-50),(0,0,255),-1)
cv2.imshow('Demo19.1',img)
cv2.waitKey(0)
cv2.destroyAllWindows()