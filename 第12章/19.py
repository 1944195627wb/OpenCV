#逼近多变形
#approxCurve = cv2.approxPolyDP(curve,epsilon,closed)
#Douglas-Peucker算法（DP算法）
import cv2
o = cv2.imread("D:/photo/wen.webp",0)
cv2.imshow("original",o)
ret,binary = cv2.threshold(o,127,255,cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
adp = o.copy()
epsilon = 0.1*cv2.arcLength(contours[0],True)
approx = cv2.approxPolyDP(contours[0],epsilon,True)
adp = cv2.drawContours(adp,[approx],0,(0,0,255),2)
cv2.imshow("result0.1",adp)

adp = o.copy()
epsilon = 0.09*cv2.arcLength(contours[0],True)
approx = cv2.approxPolyDP(contours[0],epsilon,True)
adp = cv2.drawContours(adp,[approx],0,(0,0,255),2)
cv2.imshow("result0.09",adp)

adp = o.copy()
epsilon = 0.055*cv2.arcLength(contours[0],True)
approx = cv2.approxPolyDP(contours[0],epsilon,True)
adp = cv2.drawContours(adp,[approx],0,(0,0,255),2)
cv2.imshow("result0.055",adp)

adp = o.copy()
epsilon = 0.05*cv2.arcLength(contours[0],True)
approx = cv2.approxPolyDP(contours[0],epsilon,True)
adp = cv2.drawContours(adp,[approx],0,(0,0,255),2)
cv2.imshow("result0.05",adp)

adp = o.copy()
epsilon = 0.02*cv2.arcLength(contours[0],True)
approx = cv2.approxPolyDP(contours[0],epsilon,True)
adp = cv2.drawContours(adp,[approx],0,(0,0,255),2)
cv2.imshow("result0.02",adp)
cv2.waitKey()
cv2.destroyAllWindows()