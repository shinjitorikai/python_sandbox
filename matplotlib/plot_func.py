import numpy as np
import matplotlib.pyplot as plt

# 設定値
X_MIN = -5.0
X_MAX = 5.0
Y_MIN = -0.1
Y_MAX = 1.1
X_STEP = 0.1
PLOT_TITLE = 'sigmoid function'
def func_plot(x):
  return 1 / (1+np.exp(-x))

# メイン処理
def main():
  x = np.arange(X_MIN, X_MAX, X_STEP)
  y = func_plot(x)

  plt.plot(x, y)
  plt.ylim(Y_MIN, Y_MAX) # y軸の範囲設定
  plt.xlabel('x')
  plt.ylabel('y')
  plt.grid(which='both')
  plt.title(PLOT_TITLE)
  plt.show()

if __name__ == '__main__':
    main()
