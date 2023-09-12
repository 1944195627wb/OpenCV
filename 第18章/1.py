#视频处理
#VideoCapture类
#1.初始化
#摄像头：捕获对象=cv2.VideoCapture("摄像头ID号")
#视频文件：捕获对象=cv2.VideoCapture("路径+文件名+文件形式")
#retval=cv2.VideoCapture.isOpened()——检查初始化是否成功
#retval=cv2.VideoCapture.open(index)——初始化失败打开摄像头
#retval=cv2.VideoCapture.open(filename)——处理视频文件
#捕获帧：retval,image=cv2.VideoCapture.read()
#释放None = cv2.VideoCapture.release()
#属性获取——retval=cv2.VideoCapture.get(propId)
#cv2.CAP_PROP_FRAME_WIDTH宽度
#cv2.CAP_PROP_FRAME_HEIGHT高度
#属性更改——retval=cv2.VideoCapture.set(propId,value(更改后的值))
#多个摄像头
#cv2.VideoCapture.grab()函数——指向下一帧
#retval=cv2.VideoCapture.grab()
#cv2.VideoCapture.retrieve()函数——进行解码
#retval,image=cv2.VideoCapture.retrieve()
import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret,frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) == ord('0'):
        break
cap.release()
cv2.destroyAllWindows()





