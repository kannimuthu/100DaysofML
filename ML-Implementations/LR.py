import numpy as np
x=np.array([[3,-1],[8,-1],[9,-1],[13,-1],[3,-1],[6,-1],[11,-1],[21,-1],[1,-1],[16,-1]])
y=np.array([[30],[57],[64],[72],[36],[43],[59],[90],[20],[83
   ]])
print(x)
print(y)

t1=np.linalg.inv(np.dot(x.T,x))
t2=np.dot(x.T,y)
aout=np.dot(t1,t2)
print(aout)
test=np.array([[12,-1]])
print(np.dot(aout.T,test.T))
'''y=np.dot(np.linalg.inv(np.dot(X.T,X)),np.dot(X.T,t))
print(y)
test=np.array([[10,-1]])
O=np.dot(test,y)
print(O)'''