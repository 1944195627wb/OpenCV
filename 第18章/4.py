#视频操作基础
import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret,frame = cap.read()
    frame = cv2.Canny(frame,50,200)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1)==ord(' '):
        break
cap.release()
cv2.destroyAllWindows()