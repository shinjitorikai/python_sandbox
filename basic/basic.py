
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
