import sys

# 整数(int)
#  - 範囲は無制限(利用可能な(仮想)メモリサイズの制限のみ)
print('sys.maxsize = ',sys.maxsize) # maxsizeはintの上限値ではない

# 実数(float)
#  - 範囲やマシンイプシロンなどの情報は以下参照(通常はCのdouble)
print('sys.float_info = ',sys.float_info)
#  - 無限大/非数(not a number) : これらは演算もできる
inf_plus = float('inf')
inf_minus = -float('inf')
nan = float('nan')
print('inf_plus = ',inf_plus)
print('inf_plus = ',inf_minus)
print('nan = ',nan)

# 無限大の演算
# - 和
print('inf + 1 = ',inf_plus+1) # inf
print('inf + inf = ',inf_plus+inf_plus) # inf
# - 差
print('inf - 1 = ',inf_plus-1) # inf
print('inf - inf = ',inf_plus-inf_plus) # nan
# - 積
print('inf * 0 = ',inf_plus*0) # nan
print('inf * inf = ',inf_plus*inf_plus) # inf
# - 商
print('inf / inf = ',inf_plus/inf_plus) # nan
print('0 / inf = ',0/inf_plus) # 0
#print('inf / 0 = ',inf_plus/0) # エラー
print('inf / 2 = ',inf_plus/2) # inf
# - べき
print('inf ** 0 = ',inf_plus**0) # 1
print('1 ** inf = ',1**inf_plus) # 1
print('0 ** inf = ',0**inf_plus) # 0
print('inf ** 2 = ',inf_plus**2) # inf
print('2 ** inf = ',2**inf_plus) # inf
