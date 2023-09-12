# 图像加密和解密——按位异或（相同为0，不同为1）
# xor(a,b)=c    ->xor(c,b)=a   / ->xor(c,a)=b
#a :原始数据 b:密钥 c:密文
#加密 :xor(a,b) = c  #  解密:xor(c,b)=a
import cv2
import numpy as np
img = cv2.imread("D:/photo/1.png",0)
r,c = img.shape
key = np.random.randint(0,256,size=[r,c],dtype=np.uint8)
encryption =cv2.bitwise_xor(img,key)
decryption =cv2.bitwise_xor(encryption,key)
cv2.imshow("img",img)
cv2.imshow("key",key)
cv2.imshow("encryption",encryption)
cv2.imshow("decryption",decryption)
cv2.waitKey()
cv2.destroyAllWindows()