import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-4,4,0.01)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = y3.copy()
y4[y3 > 1.1] = np.nan

plt.plot(x,y1,'-',label='sin(x)')
plt.plot(x,y2,'--',label='cos(x)')
plt.plot(x,y4,'-.',label='tan(x)')
plt.xlim([-4,4])
plt.ylim([-1.1,1.1])
plt.xlabel('x')
plt.ylabel('y')
plt.grid(which='both')
plt.title('trigonometry plot')
plt.legend()
plt.show()
