#SVM Classification
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
d=pd.read_excel("C:\\Users\\Rohini\\Desktop\\Bayes-Flu.xlsx")
d=np.asarray(d)
print(d.shape)
X=d[:,0:3]
Y=d[:,3]
print(X)
print(Y)
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3)
tree=svm.SVC(kernel="linear")
tree.fit(X_train,Y_train)
Y_pred=tree.predict(X_test)
print(Y_test)
print(Y_pred)
print("Accuracy is", accuracy_score(Y_test,Y_pred)*100)




