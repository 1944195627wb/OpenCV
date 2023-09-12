#滚动条
#cv2.createTrackbar(trackbarname,winname,value,count,onChange)
#获取滚动条的值
#retval = getTrackbarPos(trackbarname,winname)
import cv2
import numpy as np
def changeColor(x):
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    img[:]=[b,g,r]
img = np.zeros((100,700,3),np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('R','image',0,255,changeColor)
cv2.createTrackbar('G','image',0,255,changeColor)
cv2.createTrackbar('B','image',0,255,changeColor)
while True:
    cv2.imshow('image',img)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
