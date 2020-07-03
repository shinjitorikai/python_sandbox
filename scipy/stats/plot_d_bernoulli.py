# ベルヌーイ(離散)

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

p = 0.7
x = [0,1]
y = stats.bernoulli.pmf(x,p)
hist = stats.bernoulli.rvs(p,size=1000)
print('x = ',x)
print('y = ',y)

fig, axs = plt.subplots(1, 2)

axs[0].bar(x,y,width=0.1)
axs[0].set_xlim([-0.1,1.1])
axs[0].set_ylim([0,1.1])
axs[0].set_title('bernoulli.pmf(p=0.7)')
axs[0].set_xlabel('x')
axs[0].set_ylabel('probability')
axs[0].grid(which='both')

axs[1].hist(hist)
axs[1].set_xlim([-0.1,1.1])
#axs[1].set_ylim([0,1.1])
axs[1].set_title('bernoulli.rvs(p=0.7/sample=1000)')
axs[1].set_xlabel('x')
axs[1].set_ylabel('frequency')
axs[1].grid(which='both')

plt.tight_layout()
plt.show()
