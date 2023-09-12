#鼠标交互
#def OnMouseAction(event,x,y,flags,param):
#cv2.setMouseCallback(win_name,onMouse)
import cv2
import numpy as np
def Demo(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print("单击鼠标左键")
    elif event==cv2.EVENT_RBUTTONDOWN:
        print("单机了鼠标右键")
    if event==cv2.EVENT_FLAG_LBUTTON:
        print("按住左键拖动了鼠标")
    elif event==cv2.EVENT_MBUTTONDOWN:
        print("单击了中间键")
img = np.ones((300,300,3),np.uint8)*255
cv2.namedWindow('img')
cv2.setMouseCallback('img',Demo)
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()