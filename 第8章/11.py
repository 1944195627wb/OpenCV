#核函数
# retval = cv2.getStructuringElement(shape,ksize[,anchor])
#cv2.MORPH_RECT——矩形
#cv2.MORPH_CROSS——十字形结构元素
#cv2.MORPH_ELLIPSE——椭圆结构元素
import cv2
kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
kernel2 = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
kernel3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
print(kernel1)
print(kernel2)
print(kernel3)