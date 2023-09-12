# 几何变换
# 缩放： dst = cv2.resize(src,dsize[,fx[,fy[,interpolation]]])
#dsize第一个参数为宽度(列)，第二个参数是高度(行)
#fx是水平缩放比例，fy是垂直缩放比例
# dsize=Size（round（fx*src.cols）,round（fy*src.rows））
#当缩小图像时，使用区域插值方式（INTER_AREA）能够得到最好的效果；
#当放大图像时，使用三次样条插值（INTER_CUBIC）方式和双线性插值（INTER_LINEAR）方式都能够取得较好的效果。
import cv2
import numpy as np
img = np.ones([2,4,3],dtype=np.uint8)
size = img.shape[:2]
rst = cv2.resize(img,size)
print("img.shape=\n",img.shape)
print("img=\n",img)
print("rst.shape=\n",rst.shape)
print("rst=\n",rst)