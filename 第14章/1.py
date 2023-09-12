#傅里叶变换
#现图像增强、图像去噪、边缘检测、特征提取、图像压缩和加密
#返回值 = numpy.fft.fft2(原始图像)
#numpy.fft.fftshift()将零频率成分移动到频域图像的中心位置
#返回值 =numpy.fft.fftshift(原始频率)
#像素新值=20*np.log(np.abs(频谱值))
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("D:/photo/5.jpg",0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))
plt.subplot(121)
plt.imshow(img,cmap='gray')
plt.title('original')
plt.axis('off')
plt.subplot(122)
plt.imshow(magnitude_spectrum,cmap='gray')
plt.title('result')
plt.axis('off')
plt.show()