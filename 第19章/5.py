#绘制椭圆
#img == cv2.ellipse(img,center,axes,angle,startAngle,endAngle,endAngle,color[,thickness])
import numpy as np
import cv2
d = 400
img = np.ones((d,d,3),dtype='uint8')*255
center = (round(d/2),round(d/2))
size = (100,200)
for i in range(0,10):
    angle=np.random.randint(0,361)
    color = np.random.randint(0,high=256,size=(3,)).tolist()
    thickness = np.random.randint(1,9)
    cv2.ellipse(img,center,size,angle,0,360,color,thickness)
cv2.imshow("img",img)
cv2.waitKey()
cv2.destroyAllWindows()