#opencv实现傅里叶变换
#返回结果=cv2.dft(原始图像，转换标识)
#dftShift=np.fft.fftshift(dft)
#返回值=cv2.magnitude(参数1，参数2)
#result=20*np.log(cv2.magnitude(实部,虚部))
import numpy as np
import cv2
img = cv2.imread("D:/photo/5.jpg",0)
dft =cv2.dft(np.float32(img),flags=cv2.DFT_COMPLEX_OUTPUT)
print(dft)
dftShift=np.fft.fftshift(dft)
print(dftShift)
result=20*np.log(cv2.magnitude(dftShift[:,:,0],dftShift[:,:,1]))
print(result)