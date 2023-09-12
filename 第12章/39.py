#极点
# leftmost=tuple（cnt[cnt[:,:,0].argmin（）][0]）
# rightmost=tuple（cnt[cnt[:,:,0].argmax（）][0]）
# topmost=tuple（cnt[cnt[:,:,1].argmin（）][0]）
# bottommost=tuple（cnt[cnt[:,:,1].argmax（）][0]）
import cv2
import numpy as np
o = cv2.imread("D:/photo/hand.png")
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
ret,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
mask = np.zeros(gray.shape,np.uint8)
cnt = contours[0]
cv2.drawContours(mask,[cnt],0,255,-1)
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
print("leftmost=",leftmost)
print("rightmost=",rightmost)
print("topmost",topmost)
print("bottommost",bottommost)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(o,'A',leftmost,font,1,(0,0,255),2)
cv2.putText(o,'B',rightmost,font,1,(0,0,255),2)
cv2.putText(o,'C',topmost,font,1,(0,0,255),2)
cv2.putText(o,'D',bottommost,font,1,(0,0,255),2)
cv2.imshow("result",o)
cv2.waitKey()
cv2.destroyAllWindows()