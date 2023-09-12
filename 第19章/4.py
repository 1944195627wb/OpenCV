import cv2
import numpy as np
d = 400
img = np.ones((d,d,3),dtype='uint8')*255
for i in range(0,100):
    x = np.random.randint(0,high=d)
    y = np.random.randint(0,high=d)
    radius=np.random.randint(5,high=d/5)
    color=np.random.randint(0,high=256,size=(3,)).tolist()
    cv2.circle(img,(x,y),radius,color,-1)
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()
