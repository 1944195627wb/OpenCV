import cv2
o = cv2.imread("D:/photo/wen.webp",0)
ret,binary = cv2.threshold(o,127,255,cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
x,y,w,h = cv2.boundingRect(contours[0])
print("顶点及长宽的点形式：")
print("x=",x)
print("y=",y)
print("w=",w)
print("h=",h)
rect = cv2.boundingRect(contours[0])
print("\n顶点及长宽的元组(tuple)形式：")
print("rect=",rect)