import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize= (10,8))

x = [1.01,2.59,3.03,5.4,7.33,4.44]
y = [0.41,0.84,1.11,3.22,5.00,4.44]

plt.scatter(x,y)

plt.errorbar(x,y, yerr=0.2, xerr=0.1, color = 'k', linestyle = 'None')

mnk = np.polyfit(x,y,3)
z = np.poly1d(mnk)
plt.plot(np.linspace(0,10,100), [z(i) for i in np.linspace(0,10,100)])
plt.show()
