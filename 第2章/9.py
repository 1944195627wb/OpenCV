import cv2
img = cv2.imread("D:/photo/1.png")
print("读取像素点img.item(3,2,1)=",img.item(3,2,1))
img.itemset((3,2,1),255)
print("读取后像素点img.item(3,2,1)=",img.item(3,2,1))
cv2.imshow("before",img)
for i in range(10,100):
    for j in range(80,100):
            for k in range(0,3):
                img.itemset((i,j,k),255)
cv2.imshow("after",img)
cv2.waitKey()
cv2.destoryAllWindows()
