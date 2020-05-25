import numpy as np

# 1次元配列
A = np.array([1,2,3,4])

print('1次元配列 A = ', A)

print(' - 配列の型 : ', type(A))
print(' - 配列要素の型 : ', A.dtype)

print(' - 配列次元数 = ', np.ndim(A)) # 結果はタプル
print(' - 配列の形状 = ', A.shape)
print(' - 配列の形状(タプルの0番目) = ', A.shape[0])

print(' - 要素アクセス : A[0] = ', A[0])

print(' - 配列による要素アクセス : ', A[np.array([0,2])])
print(' - 論理演算 : ', A>=3)
print(' - 配列による要素アクセス : ', A[A>=3])

# 2次元配列
B = np.array([[1,2], [3,4], [5,6]])

print('2次元配列 B = ', B)

print(' - 配列の型 : ', type(B))
print(' - 配列要素の型 : ', B.dtype)

print(' - 配列次元数 = ', np.ndim(B)) # 結果はタプル
print(' - 配列の形状 = ', B.shape)

print(' - 要素アクセス : B[0] = ', B[0]) # 0行目
print(' - 要素アクセス : B[0][1] = ', B[0][1]) # 0行目1列目
for row in B:
    print(' - 要素アクセス : for = ', row)

print(' - 1次元へ変換 : ', B.flatten())

# 行列の積(ドット積)
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

print('A = ', A)
print('B = ', B)

print('A・B = ', np.dot(A,B))
