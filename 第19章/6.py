#绘制多边形
#img = cv2.polylines(img,pts,isClosed,color[,thickness[,lineType[,shift]]])
import numpy as np
import cv2
d = 400
img = np.ones((d,d,3),dtype='uint8')*255
pts = np.array([[200,50],[300,200],[200,350],[100,200]],np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(255,255,0),8)
print(pts)
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()