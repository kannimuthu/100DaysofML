import matplotlib.pyplot as plt
import numpy as np
label = ['DT','SVM','NB']
accuracy=[80,85.5,90]
plt.barh (label,accuracy)
plt.xlabel('Accuracy(%)', fontsize=15)
plt.ylabel('Algorithm', fontsize=15)
plt.title('ML Algorithm Comparison')
plt.show()