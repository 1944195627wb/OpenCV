#x,y不能同时设置1
import cv2
import numpy as np
o=cv2.imread("D:/photo/cat2.webp")
Scharrxy11 = cv2.Scharr(o,cv2.CV_64F,1,1)
Scharrxy11 = cv2.convertScaleAbs(Scharrxy11)
cv2.imshow("original",o)
cv2.imshow("xy11",Scharrxy11)
cv2.waitKey()
cv2.destroyAllWindows()