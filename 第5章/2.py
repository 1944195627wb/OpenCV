import cv2
img = cv2.imread("D:/photo/1.png")
rows,cols = img.shape[:2]
size = (int(cols*0.9),int(rows*0.5))
rst = cv2.resize(img,size)
print("img.shape=\n",img.shape)
print("rst.shape=\n",rst.shape)
