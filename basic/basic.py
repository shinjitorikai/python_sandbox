
a = 1

# data type : type()関数でデータの型を調べることができる
print('type = ',type(a))
print('type = ',type(3.14))
print('type = ',type("abc"))

# list
listdata = [1,2,3,4,5]
print('listdata = ', listdata)
print(' - type = ', type(listdata))
print(' - length = ', len(listdata))
print(' - 要素アクセス a[0] = ', listdata[0])
print(' - スライシング a[0:2] = ', listdata[0:2]) # 0番目から2番目まで(2番目は含まない)
print(' - スライシング a[2:] = ', listdata[2:]) # 2番目以降
print(' - スライシング a[:2] = ', listdata[:2]) # 2番目まで(2番目は含まない)
print(' - スライシング a[:-1] = ', listdata[:-1]) # 最後から1つ前まで(最後から1つ前は含まない)
print(' - スライシング a[:-2] = ', listdata[:-2]) # 最後から2つ前まで(最後から2つ前は含まない)

# dictionary
dicdata = {'key1':12,'key2':34,'key4':78}
print('dicdata = ', dicdata)
print('dicdata(type) = ', type(dicdata))
print('dicdata(len) = ', len(dicdata))
print(' - 要素アクセス key1 : ', dicdata['key1'])
dicdata['key3'] = 56
print(' - 要素追加 : ', dicdata)
dicdata2 = {} # dictionaryの初期化
print('dicdata2 = ', dicdata2)

# logical calc
bData1 = True
bData2 = False
print('論理演算')
print(' - not bData1 : ', not bData1)
print(' - and bData1 : ', bData1 and bData2)
print(' - or  bData1 : ', bData1 or bData2)

# reversed/enumerate
r = range(3)
print('range(3) = ',r) # range(0, 3)
r_l = list(r)
print('list(range(3)) = ',r_l) # [0, 1, 2]
r_rev = reversed(r)
print('reversed(range(3)) = ',r_rev) # <range_iterator object>(逆転)
print('list(reversed(range(3))) = ',list(r_rev)) # [2, 1, 0]

# zip
list1 = [1,2,3,4]
list2 = ['A','B','C']
list_zip = zip(list1,list2)
print('zip(list1,list2) = ',list_zip) # <zip object>
print('zip(list1,list2) = ',list(list_zip)) # [(1, 'A'), (2, 'B'), (3, 'C')] (多い方は無視)

# enumerate
r_e = enumerate(list2)
print('enumerate(list2) = ',r_e)
print('list(enumerate(list2)) = ',list(r_e))

# リスト内包表記(list)
tmp1 = [i*2 for i in range(3)]
print('[i*2 for i in range(3)] = ',tmp1)
tmp2 = [i for i in range(10) if i%2==0]
print('[i for i in range(10) if i%2==0] = ',tmp2)

# 集合内包表記(set)
tmp3 = {i*2 for i in range(3)}
print('{i*2 for i in range(3)} = ',tmp3)

# 辞書内包表記(dictionaryの生成)
tmp4 = ['A','B','C'] # list
tmp5 = {v:i for i,v in enumerate(tmp4)}
print('{v:i for i,v in enumerate(tmp4)} = ',tmp5) # {'A': 0, 'B': 1, 'C': 2}

# イテレーター
it = iter(list1)
print('iter(list1) = ',it) # <list_iterator object>
print('next(it) = ',next(it)) # 1
print('next(it) = ',next(it)) # 2
