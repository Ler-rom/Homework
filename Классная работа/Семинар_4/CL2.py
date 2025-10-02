import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize= (10,8))

x = [1.01,2.59,3.03,5.4,7.33,4.44]
y = [0.41,0.84,1.11,3.22,5.00,7.8]

plt.scatter(x,y)

plt.errorbar(x,y, yerr=0.2, xerr=0.1, color = 'k', linestyle = 'None')

mnk = np.polyfit(x,y,1)
z = np.poly1d(mnk)
plt.plot([0,9],[z(0),z(9)])
plt.show()
