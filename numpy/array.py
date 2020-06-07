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

# rangeによる生成
A2 = np.arange(-1.0,1.0,0.1)
print('A2(arange) = ',A2)
print('A2 shape = ',A2.shape)
A2_2 = range(0,5) # 補足 : Numpyではない
print('A2_2 = ',A2_2)
print('A2_2(list) = ',list(A2_2))
A2_3 = range(0,10,3) # 補足 : Numpyではない
print('A2_3 = ',A2_3)
print('A2_3(list) = ',list(A2_3))

# broadcast
#  - スカラー値とNumpy配列との演算は、スカラー値とNumpy配列の各要素同士で行われる
A3 = np.array([1.0,2.0,3.0])
print('A3 = ',A3)
print('A3 + 1.0 = ',A3+1.0)

# 和
print('np.sum(np.array([1.0,2.0,3.0]) = ',np.sum(np.array([1.0,2.0,3.0])))
print('np.sum(np.array([[1.0,2.0],[3.0,4.0]]) = ',np.sum(np.array([[1.0,2.0],[3.0,4.0]])))

# 最大値
argmaxtest = np.array([[1,9,3],[6,5,8],[7,2,4]])
print('argmax.shape = ',argmaxtest.shape)
print('argmax : ',np.argmax(argmaxtest))
print('argmax(axis=0) : ',np.argmax(argmaxtest,axis=0))
print('argmax(axis=1) : ',np.argmax(argmaxtest,axis=1))

# サイズの変形
A4 = np.array([1,2,3,4,5,6,7,8,9])
print('A4 = ',A4)
print('A4(reshape) = ',A4.reshape(3,3))

# 行列の作成
print('random = ',np.random.randint(low=0,high=10,size=(2,3)))
