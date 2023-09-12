import numpy as np
import cv2
cap = cv2.VideoCapture("D:/video/tanker_game.mp4")
while cap.isOpened():
    ret,frame = cap.read()
    cv2.imshow("frame",frame)
    c = cv2.waitKey(25)
    if c ==27:
        break
cap.release()
cv2.destroyAllWindows()