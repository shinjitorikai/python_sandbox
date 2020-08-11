# 統計関連基礎
import math
import scipy.special
import pandas as pd

# 階乗
print('3! = ',math.factorial(3))

# 順列(nPr)
print('6P4 = ',scipy.special.perm(6,4))

# 組み合わせ(nCr)
print('6C4 = ',scipy.special.comb(6,4))

# 平均/中央値/最頻値/分散/標準偏差
df = pd.DataFrame({'Data':[100,150,200,150,300,500,250,150]})
print(df)
print('平均値 : ',df['Data'].mean())
print('中央値 : ',df['Data'].median())
print('最頻値 : ',(df['Data'].mode())[0])
print('分散 : ', df['Data'].var())
print('標準偏差 : ', df['Data'].std())

# いろいろな統計量をまとめて表示
print(df.describe())
