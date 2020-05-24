import numpy as np

# 1次元配列
A = np.array([1,2,3,4])

print('1次元配列 A = ')
print(A)

print(' - 配列次元数 = ')
print(np.ndim(A)) # 結果はタプル

print(' - 配列の形状 = ')
print(A.shape)

print(' - 配列の形状(タプルの0番目) = ')
print(A.shape[0])

# 2次元配列
B = np.array([[1,2], [3,4], [5,6]])

print('2次元配列 B = ')
print(B)

print(' - 配列次元数 = ')
print(np.ndim(B)) # 結果はタプル

print(' - 配列の形状 = ')
print(B.shape)

# 行列の積(ドット積)
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

print('A = ')
print(A)

print('B = ')
print(B)

print('A・B = ')
print(np.dot(A,B))
