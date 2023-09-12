# OpenCV通过函数cv2.face.EigenFaceRecognizer_create（）生成特征
# 脸识别器实例模型，然后应用 cv2.face_FaceRecognizer.train（）函数完
# 成训练，最后用 cv2.face_FaceRecognizer.predict（）函数完成人脸识别。
import cv2
import numpy as np
images= []
images.append(cv2.imread("e01.png", 0))
images.append(cv2.imread('e02.png',0))
images.append(cv2.imread('e11.png',0))
images.append(cv2.imread('e12.png',0))
labels=[0,0,1,1]
print(labels)
recognizer=cv2.faceEigenRecognizer_create()
recognizer.train(images,np.array(labels))
predict_image=cv2.imread('eTest.png',cv2.IMREAD_GRAYSCALE)
label,confidence=recognizer.predict(predict_image)
print('label=',label)
print('confidence=',confidence)
