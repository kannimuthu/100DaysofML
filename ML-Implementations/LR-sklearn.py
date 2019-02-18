import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
years=[0,1,2,3,4]
sales=[12,19,29,37,45]
X=np.array([years]).T
Y=np.array(sales)
X_new=[5,6,7,8]
X_new=np.array([X_new]).T
r=LinearRegression()
r=r.fit(X,Y)
print(r.coef_)
print(r.intercept_)
predict_Y=r.predict(X_new)
print(predict_Y)
#print('meansquare',mean_squared_error(Y,predict_Y))
#print('RMSE',np.sqrt(mean_squared_error(Y,predict_Y)))