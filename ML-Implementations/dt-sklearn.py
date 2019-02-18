import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
d=pd.read_excel("C:\\Users\\Rohini\\Desktop\\Bayes-Flu.xlsx")
d=np.asarray(d)
print(d)
X=d[:,0:3]
Y=d[:,3]
print(X)
print(Y)
r=DecisionTreeClassifier(criterion="entropy")
r=r.fit(X,Y)
predict_Y=r.predict(X)
print(predict_Y)
print('Accuracy',accuracy_score(Y,predict_Y)*100)
print('CM',confusion_matrix(Y,predict_Y))



