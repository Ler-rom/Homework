import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize = (10,8))

ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
ax2 = fig.add_axes([0.2,0.5,0.4,0.3])

x = np.arange(0,10)
y = x**2

ax1.plot(x,y,'r')
ax2.plot(x,y)
plt.show()


