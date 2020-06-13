import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = np.arange(-1,1,0.05)
y = np.arange(-1,1,0.05)
X,Y = np.meshgrid(x,y)
Z = X**2 + Y**2

sns.heatmap(Z,vmin=0.0,vmax=1.5)
plt.show()
