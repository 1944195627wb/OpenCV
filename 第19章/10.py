import cv2
import numpy as np
d = 400
def draw(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        p1x = x
        p1y = y
        p2x = np.random.randint(1,d-50)
        p2y = np.random.randint(1,d-50)
        color = np.random.randint(0,high=256,size=(3,)).tolist()
        cv2.rectangle(img,(p1x,p1y),(p2x,p2y),color,2)
img = np.ones((d,d,3),dtype='uint8')*255
cv2.namedWindow('Demo')
cv2.setMouseCallback('Demo',draw)
while True:
    cv2.imshow('Demo',img)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()