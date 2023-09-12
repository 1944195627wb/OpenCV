#绘制圆形
#img = cv2.circle(img,center,radius,color[,thickness[,lineType]])
#round函数——用于
import numpy as np
import cv2
d = 400
img = np.ones((d,d,3),dtype='uint8')*255
(x,y) = (round(img.shape[1]/2),round(img.shape[0]/2))
red = (0,0,255)
for r in range(5,round(d/2),12):
    cv2.circle(img,(x,y),r,red,3)
cv2.imshow("Demo19.3",img)
cv2.waitKey()
cv2.destroyAllWindows()