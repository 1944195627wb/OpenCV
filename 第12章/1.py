#图像轮廓——连接起来形成的一个整体#灰度二值图
#查找图像的轮廓信息——cv2.findContours()
#绘制图像轮廓——cv2.drawContours()
#img,contours,hierarchy = cv2.findContours(image,mode,method)(4.x版本无img返回值)
#cv2.RETR_EXTERNAL：只检测外轮廓。
#cv2.RETR_LIST：对检测到的轮廓不建立等级关系。
#cv2.RETR_CCOMP：检索所有轮廓并将它们组织成两级层次结构。上面的一层为外边界，下面的一层为内孔的边界。如果内孔内还有一个连通物体，那么这个物体的边界仍然位于顶层。
#cv2.RETR_TREE：建立一个等级树结构的轮廓。
# 参数method决定了如何表达轮廓，可以为如下值：
# cv2.CHAIN_APPROX_NONE：存储所有的轮廓点，相邻两个点的像素位置差不超过1，即max（abs（x1-x2）,abs（y2-y1）=1。
# cv2.CHAIN_APPROX_SIMPLE：压缩水平方向、垂直方向、对角线方向的元素，只保留该方向的终点坐标。例如，在极端的情况下，一个矩形只需要用4个点来保存轮廓信息。
# cv2.CHAIN_APPROX_TC89_L1：使用teh-Chinl chain近似算法的一种风格。
# cv2.CHAIN_APPROX_TC89_KCOS：使用teh-Chinl chain近似算法的一种风格。
#image=cv2.drawContours(image,contours,contourIdx,color[,thickness[,lineType[,hierarchy[,maxLevel[,offset]]]]])
import cv2
o = cv2.imread("D:/photo/wen.webp")
cv2.imshow("original",o)
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
ret,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours,hierarchy =cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
o =cv2.drawContours(o,contours,-1,(255,255,0),2)
cv2.imshow("result",o)
cv2.waitKey()
cv2.destroyAllWindows()