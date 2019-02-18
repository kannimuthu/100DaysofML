import matplotlib.pyplot as plt
print(plt.style.available)
plt.style.use('seaborn-whitegrid')
import numpy as np
#fig = plt.figure()
#ax = plt.axes()
#x = np.linspace(0, 10, 1000)
#plt.plot(x, np.sin(x))
#plt.plot(x, np.cos(x));
a=[1,2,3,4,5]
b=[2,4,6,8,10]
#plt.xlim(2,10)
##plt.plot(a,b,"-g")
##plt.plot(a,b,"--c")
##plt.plot(a,b,":r")
plt.plot(a,b,"-.b")


