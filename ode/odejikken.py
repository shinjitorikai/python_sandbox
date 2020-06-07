# Pythonによる常微分方程式のソルバーのテスト

# 参考：
# https://www.sejuku.net/blog/74879

# 微分方程式：
# dy/dx = ay

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def func(y, x, a):
  dydx = a * y
  return dydx

a = 1
y0 = 1
x = np.arange(0, 3, 0.01)

y = odeint(func, y0, x, args=(a,)) # 補足 : argsパラメーターはタプル

def func_validate(x): # 答えを確認するためのもの(解析解)
  return np.exp(x)

plt.plot(x, y, label='solve')
plt.plot(x, func_validate(x), label='validate')
plt.xlabel('x')
plt.xlim(0,3)
plt.ylabel('y')
plt.ylim(0,20)
plt.legend()
plt.grid(True)
plt.show()
