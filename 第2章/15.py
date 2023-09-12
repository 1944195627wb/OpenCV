import cv2
tong = cv2.imread("D:/photo/3.jpg",cv2.IMREAD_UNCHANGED)
bo = cv2.imread("D:/photo/4.jpg",cv2.IMREAD_UNCHANGED)
cv2.imshow("tong",tong)
cv2.imshow("bo",bo)
tong_face = tong[500:1000,200:700]
bo[400:900,400:900] = tong_face
cv2.imshow("result",bo)
cv2.waitKey()
cv2.destoryAllWindows()

