import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = np.arange(-1,1,0.2)
y = np.arange(-1,1,0.2)
X,Y = np.meshgrid(x,y)
Z = X**2 + Y**2

sns.heatmap(Z,vmin=0.0,vmax=2.0,annot=True)
plt.show()
