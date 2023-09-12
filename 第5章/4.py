#翻转
#dst = cv2.flip(src,flipCode)
#0->绕x
#正->绕y
#负->绕x,y
# flicCode=0->srcsrc.rows-i-1,j
# flipCode>0->srci,src.cols-j-1
# flipCode<0->srcsrc.rows-i-1,src.cols-j-1
import cv2
img = cv2.imread("D:/photo/1.png")
x = cv2.flip(img,0)
y = cv2.flip(img,1)
xy = cv2.flip(img,-1)
cv2.imshow("img",img)
cv2.imshow("x",x)
cv2.imshow("y",y)
cv2.imshow("xy",xy)
cv2.waitKey()
cv2.destroyAllWindows()