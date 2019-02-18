import matplotlib.pyplot as plt
import numpy as np
label = ['DT','SVM','NB']
accuracy=[80,85.5,90]
index = np.arange(len(label))
plt.bar(index, accuracy)
plt.xlabel('Algorithm', fontsize=15)
plt.ylabel('Accuracy(%)', fontsize=15)
plt.xticks(index, label, fontsize=15, rotation=30)
plt.title('ML Algorithm Comparison')
plt.show()