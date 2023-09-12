#实现逆傅里叶变换
#返回结果=cv2.idft(原始数据)
import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread("D:/photo/5.jpg",0)
dft =cv2.dft(np.float32(img),flags=cv2.DFT_COMPLEX_OUTPUT)
dftShift = np.fft.fftshift(dft)
ishift = np.fft.ifftshift(dftShift)
iImg = cv2.idft(ishift)
iImg = cv2.magnitude(iImg[:,:,0],iImg[:,:,1])
plt.subplot(121),plt.imshow(img,cmap='gray')
plt.title('original'),plt.imshow(iImg,cmap='gray')
plt.title('inverse'),plt.axis('off')
plt.show()