# 在OpenCV中，通过函数cv2.face.FisherFaceRecognizer_create（）生成Fisherfaces识别器实例模型，然后应用
# cv2.face_FaceRecognizer.train（）函数完成训练，用
# cv2.face_FaceRecognizer.predict（）函数完成人脸识别。
import cv2
import numpy as np
images=[]
images.append(cv2.imread('f01.png',0))
images.append(cv2.imread('f02.png',0))
images.append(cv2.imread('f11.png',0))
images.append(cv2.imread('f12.png',0))
labels=[0,0,1,1]
print(labels)
recognizer=cv2.face.FisherFaceRecongnizer_create()
recognizer.train(images,np.array(labels))
predict_image=cv2.imread('fTest.png',cv2.IMREAD_GRAYSCALE)
label,confidence=recognizer.predict(predict_image)
print("label=",label)
print('confidence=',confidence)
