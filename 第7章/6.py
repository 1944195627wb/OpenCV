#高斯滤波——会将中心点的权重值加大，远离中心点的权重值减小
#在高斯滤波中，核的宽度和高度可以不相同，但是它们都必须是奇数
#dst = cv2.GaussianBlur(src,ksize,sigmaX,sigmaY,borderType)
#若sigmaX和sigmaY都为0
#sigmaX=0.3×[（ksize.width-1）×0.5-1]+0.8
#sigmaY=0.3×[（ksize.height-1）×0.5-1]+0.8
import cv2
img = cv2.imread("D:/photo/16.jpg")
result = cv2.GaussianBlur(img,(5,5),0,0)
cv2.imshow("img",img)
cv2.imshow("result",result)
cv2.waitKey()
cv2.destroyAllWindows()


