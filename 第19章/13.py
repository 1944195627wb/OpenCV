#用滚动条控制阈值处理参数
#retval,dst = cv2.threshold(src,thresh,maxval,type)
import cv2
Type = 0
Value=0
def onType(a):
    Type = cv2.getTrackbarPos(tType,windowName)
    Value = cv2.getTrackbarPos(tValue,windowName)
    ret,dst = cv2.threshold(o,Value,255,Type)
    cv2.imshow(windowName,dst)
def onValue(a):
    Type = cv2.getTrackbarPos(tType,windowName)
    Value = cv2.getTrackbarPos(tValue,windowName)
    ret,dst = cv2.threshold(o,Value,255,Type)
    cv2.imshow(windowName,dst)
o = cv2.imread('D:/photo/1.png',0)
windowName = 'Demo'
cv2.namedWindow(windowName)
tType ='Type'
tValue = 'Value'
cv2.createTrackbar(tType,windowName,0,4,onType)
cv2.createTrackbar(tValue,windowName,0,255,onValue)
if cv2.waitKey(0)==27:
    cv2.destroyAllWindows()