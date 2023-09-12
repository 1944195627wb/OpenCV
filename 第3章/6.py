import cv2
tong = cv2.imread("D:/photo/3.jpg",cv2.IMREAD_UNCHANGED)
bo = cv2.imread("D:/photo/4.jpg",cv2.IMREAD_UNCHANGED)
cv2.imshow("tong",tong)
cv2.imshow("img2",bo)
face1 = tong[500:1000,200:700]
face2 = bo[400:900,400:900]
add = cv2.addWeighted(face1,0.6,face2,0.4,0)
bo[400:900,400:900] = add
cv2.imshow("result",bo)
cv2.waitKey()
cv2.destroyAllWindows()