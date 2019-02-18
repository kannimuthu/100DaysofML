import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plot
import pandas as pd
d=pd.read_csv("C:\\Users\\Rohini\\Desktop\\Nandha\\PCA.csv")
A=np.asarray(d)
print(A.shape)
plot.scatter(A[:,0:1],A[:,1:2])
pca = PCA(n_components = 2)
pca.fit(A)
# reconstruct image with independent components
td = pca.fit_transform(A)
rd = pca.inverse_transform(td)
print(td)
print(rd)