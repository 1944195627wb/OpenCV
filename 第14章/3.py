import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("D:/photo/5.jpg",0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
rows,cols =img.shape
crow,ccols= int(rows/2),int(cols/2)
fshift[crow-30:rows+30,ccols-30:ccols+30]=0
ishift=np.fft.ifftshift(fshift)
iimg = np.fft.ifft2(ishift)
iimg = np.abs(iimg)
plt.subplot(121),plt.imshow(img,cmap='gray')
plt.title('original'),plt.axis('off')
plt.subplot(122),plt.imshow(iimg,cmap='gray')
plt.title('iimg'),plt.axis('off')
plt.show()