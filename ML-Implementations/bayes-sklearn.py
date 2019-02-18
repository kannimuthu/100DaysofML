import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
#from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
d=pd.read_excel("C:\\Users\\Rohini\\Desktop\\Bayes-Flu.xlsx")
d=np.asarray(d)
print(d.shape)
X=d[:,0:3]
Y=d[:,3]
print(X)
print(Y)
r=MultinomialNB()
#r=GaussianNB()
r=r.fit(X,Y)
#print(r.class_prior)
print(r.class_count_)
print(r.classes_)
predict_Y=r.predict(X)
print(predict_Y)
print('Accuracy',accuracy_score(Y,predict_Y)*100)
print('CM',confusion_matrix(Y,predict_Y))



