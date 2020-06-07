from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca(projection='3d')

theta = np.linspace(-2 * np.pi, 2 * np.pi, 100)
r = theta
x = np.sin(theta)
y = np.cos(theta)

ax.plot(x, y, theta, label='spiral')
ax.legend()

plt.show()
