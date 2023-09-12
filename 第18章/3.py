#VideoWriter类
#<VideoWriter_object>=cv2.VideoWriter(filename,fourcc,fps,frameSize[,isColor])
#fourcc=cv2.VideoWriter_fourcc(*'XVID')
#out=cv2.VideoWriter('output.avi',fourcc,20,(1024,768))
#write函数()
#None=cv2.VideoWriter.write(image)
#None = cv2.VideoWriter.release()
#保存视频
import numpy as np
import cv2
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('I','4','2','0')
out = cv2.VideoWriter('output.avi',fourcc,20,(640,480))
while cap.isOpened():
    ret,frame = cap.read()
    if ret:
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1)==27:
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
