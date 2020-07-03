from pathlib import Path

target_dir = 'C:\\test'

pt = Path(target_dir)
print('pt : ',pt)
print(' - type : ',type(pt))
print(' - to string : ',pt.as_posix())
print(' - to string : ',str(pt))

# ターゲットディレクトリの、ファイルおよびフォルダを取得
#print(list(pt.glob('*'))) # list化して表示
for f in pt.glob('*'):
    print(f)

print('/// 検索条件あり ///')
for f in pt.glob('*.sln'): # 条件あり
    print(f)

print('/// サブディレクトリも含む ///')
for f in pt.glob('**/*'): # サブディレクトリも含む
    print(f)
