#1.级联分类器
#2.Haar级联分类器
import cv2
image=cv2.imread("D:/photo/4.jpg")
faceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces=faceCascade.detectMultiScale(gray,scaleFactor=1.15,minNeighbors=5,minSize=(5,5))
print(faces)
print("发现{}个人脸！".format(len(faces)))
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)
    cv2.circle(image,(int((x+x+w)/2),int((y+y+h)/2)),int(w/2),(0,255,0),2)
cv2.imshow("dect",image)
cv2.imwrite("re.jpg",image)
cv2.waitKey()