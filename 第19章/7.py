#绘制文字
#img = cv2.putText(img,text,org,fontFace,fontScale,color[thickness[,lineType])
import numpy as np
import cv2
d = 400
img = np.ones((d,d,3),dtype='uint8')*255
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(0,200),font,3,(0,255,0),15)
cv2.putText(img,'OpenCV',(0,200),font,3,(0,0,255),5)
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()