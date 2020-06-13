import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-1,1,0.05)
y = np.arange(-1,1,0.05)
X,Y = np.meshgrid(x,y)
Z = X**2 + Y**2

fig = plt.figure()
aa = plt.pcolormesh(X,Y,Z,cmap='plasma')
fig.colorbar(aa)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# 補足:cmapの設定値
# https://matplotlib.org/examples/color/colormaps_reference.html
