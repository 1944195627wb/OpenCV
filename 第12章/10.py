#形状匹配
#retval =cv2.matchShapes(contour1,contour2,method,parameter)
#方法
#cv2.CONTOURS_MATCH_11(12/13)
import cv2
o1 = cv2.imread("D:/photo/me1.png",0)
o2 = cv2.imread("D:/photo/me2.png",0)
o3 = cv2.imread("D:/photo/me_destroy.png",0)
ret1,binary1 = cv2.threshold(o1,127,255,cv2.THRESH_BINARY)
ret2,binary2 = cv2.threshold(o2,127,255,cv2.THRESH_BINARY)
ret3,binary3 = cv2.threshold(o3,127,255,cv2.THRESH_BINARY)
contours1,hierarchy1 = cv2.findContours(binary1,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
contours2,hierarchy2 = cv2.findContours(binary2,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
contours3,hierarchy3 = cv2.findContours(binary3,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cnt1 = contours1[0]
cnt2 = contours2[0]
cnt3 = contours3[0]
ret_1 = cv2.matchShapes(cnt1,cnt2,1,0.0)
ret_2 = cv2.matchShapes(cnt2,cnt3,1,0.0)
ret_3 = cv2.matchShapes(cnt1,cnt3,1,0.0)
print("1和2",ret_1)
print("2和3",ret_2)
print("1和3",ret_3)

