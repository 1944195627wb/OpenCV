#svm = cv2.ml.SVM_create()
#训练结果=svm.train（训练数据，训练数据排列格式，训练数据的标签）
#cv2.ml.ROW_SAMPLE每条训练数据占一行
#cv2.ml.ROW_SAMPLE每条训练数据占一列
#返回值=svm.train(data,cv2.ml.ROW_SAMPLE,label)
#（返回值，返回结果）=svm.predict（测试数据）
import cv2
import matplotlib.pyplot as plt
import numpy as np
a = np.random.randint(95,100,(20,2)).astype(np.float32)
b= np.random.randint(90,95,(20,2)).astype(np.float32)
data = np.vstack((a,b))
data=np.array(data,dtype='float32')
aLabel=np.zeros((20,1))
bLabel=np.ones((20,1))
label=np.vstack((aLabel,bLabel))
label=np.array(label,dtype='int32')
svm = cv2.ml.SVM_create()
result=svm.train(data,cv2.ml.ROW_SAMPLE,label)
test=np.vstack([[98,90],[90,99]])
test = np.array(test,dtype='float32')
(p1,p2)=svm.predict(test)
plt.scatter(a[:,0],a[:,1],80,'g','o')
plt.scatter(b[:,0],b[:,1],80,'b','s')
plt.scatter(test[:,0],test[:1],80,'r','*')
print(test)
print(p2)
plt.show()
