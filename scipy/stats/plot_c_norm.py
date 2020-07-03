# 正規(連続)

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

p = 0.7
x = np.linspace(stats.norm.ppf(0.01),stats.norm.ppf(0.99),100)
y = stats.norm.pdf(x)
hist = stats.norm.rvs(size=1000)
print('x = ',x)
print('y = ',y)

fig, axs = plt.subplots(1, 2)

axs[0].plot(x,y)
#axs[0].set_xlim([-0.1,1.1])
axs[0].set_ylim([0,1.1])
axs[0].set_title('norm.pdf(p=0.7)')
axs[0].set_xlabel('x')
axs[0].set_ylabel('probability')
axs[0].grid(which='both')

axs[1].hist(hist)
#axs[1].set_xlim([-0.1,1.1])
#axs[1].set_ylim([0,1.1])
axs[1].set_title('norm.rvs(size=1000)')
axs[1].set_xlabel('x')
axs[1].set_ylabel('frequency')
axs[1].grid(which='both')

plt.tight_layout()
plt.show()
