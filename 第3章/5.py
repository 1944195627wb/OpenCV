#加权和
import cv2
img1 = cv2.imread("D:/photo/6.webp")
img2 = cv2.imread("D:/photo/7.webp")
result = cv2.addWeighted(img1,0.6,img2,0.4,0)
cv2.imshow("dog1",img1)
cv2.imshow("dog2",img2)
cv2.imshow("result",result)
cv2.waitKey()
CV2.destroyAllWindows()