#numpy.fft.ifftshift()将零频率分量移到原来的位置
#调整后的频谱=numpy.fft.ifftshift(原始频谱)
#numpy.fft.iff2函数可以进行实现逆傅里叶变化
#返回值=numpy.fft.ifft2(频域数据)
#iimg = np.abs(逆傅里叶变换结果)
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("D:/photo/5.jpg",0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
ishift=np.fft.ifftshift(fshift)
iimg = np.fft.ifft2(ishift)
iimg = np.abs(iimg)
plt.subplot(121),plt.imshow(img,cmap='gray')
plt.title('original'),plt.axis('off')
plt.subplot(122),plt.imshow(iimg,cmap='gray')
plt.title('iimg'),plt.axis('off')
plt.show()