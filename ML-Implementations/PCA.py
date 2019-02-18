import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plot
A=np.array([[1,1],[2,4],[3,7],[4,11],[5,9]])
plot.scatter(A[:,0:1],A[:,1:2])
pca = PCA(n_components = 1)
pca.fit(A)
# reconstruct image with independent components
td = pca.fit_transform(A)
rd = pca.inverse_transform(td)
print(td)
print(rd)