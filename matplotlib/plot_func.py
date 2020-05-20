import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
  return 1 / (1+np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1) # y軸の範囲設定
plt.xlabel('x')
plt.ylabel('y')
plt.grid(which='both')
plt.title('sigmoid function')
plt.show()
