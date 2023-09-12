#脸部打码及解码
import cv2
import numpy as np
#读取原始载体图像
img = cv2.imread("D:/photo/1.png",0)
#读取原始载体图像的shape值
w,h = img.shape
mask = np.zeros((w,h),dtype=np.uint8)
mask[100:800,100:700] = 1
#获取一个key,打码、解码所使用的密钥
key = np.random.randint(0,256,size=[w,h],dtype=np.uint8)
#获取打码脸
#使用key对原始图像img加密
imgXorKey = cv2.bitwise_xor(img,key)
#获取加密图像的脸部信息encryptFace
encryptFace = cv2.bitwise_and(imgXorKey,mask*255)
#将图像img内部的脸部值设置为0，得到noFace1
noFace1 = cv2.bitwise_and(img,(1-mask)*255)
#得到打码的img图像
maskFace = encryptFace + noFace1
#将脸部打码的img与密钥key进行异或运算，得到脸部的原始信息
extractOriginal = cv2.bitwise_xor(maskFace,key)
#将解码的脸部信息extractOriginal提取出来，得到extractFace
extractFace = cv2.bitwise_and(extractOriginal,mask*255)
#从脸部打码的img内提取没有脸部信息的img图像，得到noFace2
noFace2 = cv2.bitwise_and(maskFace,(1-mask)*255)
#得到解码的img图像
extractImg = noFace2+extractFace
#显示图像
cv2.imshow("img",img)
cv2.imshow("mask",mask*255)
cv2.imshow("1-mask",(1-mask)*255)
cv2.imshow("key",key)
cv2.imshow("imgXorKey",imgXorKey)
cv2.imshow("encryptFace",encryptFace)
cv2.imshow("noFace1",noFace1)
cv2.imshow("maskFace",maskFace)
cv2.imshow("extractFace",extractFace)
cv2.imshow("noFace2",noFace2)
cv2.imshow("extractImg",extractImg)
cv2.waitKey()
cv2.destroyAllWindows()