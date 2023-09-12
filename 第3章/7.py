#按位逻辑运算
#按位与 —————dst = cv2.bitwise_and(src1,src2[,mask]])
#N-0 ->0
#N-255 ->N
#按位或——dst = cv2.bitwise_or(src1,src2[,mask]])
#按位非——dst = cv2.bitwise_not(src[,mask]])
#按位异或——dst = cv2.bitwise_xor(src1,src2[,mask])
import cv2
a = np.random.randint(0,255,(5,5),dtype = np.uint8)
b = np.zeros((5,5),dtype=np.uint8)
b[0:3,0:3]=255
b[4,4]=255
c = cv2.bitwise_and(a,b)
print("a=\n",a)
print("b=\n",b)
print("c=\n",c)

