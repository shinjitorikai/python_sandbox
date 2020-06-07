from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def func1(x, y):
    return (x**2 + 2*y**2) - 3

x = np.arange(-1.0, 1.0, 0.05)
y = np.arange(-1.0, 1.0, 0.05)
X, Y = np.meshgrid(x, y)
Z = func1(X, Y)

fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("f(x, y)")
ax.plot_wireframe(X, Y, Z)
plt.show()
