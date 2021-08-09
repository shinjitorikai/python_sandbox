from pathlib import Path
from tqdm import tqdm

# 設定値
target_dir = r'F:\整理中'
#search_cond = '*' # ターゲットディレクトリの、ファイルおよびフォルダを取得
#search_cond = '*.sln' # 条件あり
search_cond = '**/*' # サブディレクトリも含む
output_filename = r'.\filesystem\output.csv'


# ファイル/フォルダを取得
print('ファイル/フォルダを取得...')
pt = Path(target_dir)
resultlist = list(pt.glob(search_cond))

# 結果をファイルに出力
print('結果をファイルに出力...')
#with open(output_filename,mode='w',encoding='utf-8') as fw: # utf-8だとExcelで開いたときに文字化け
with open(output_filename,mode='w') as fw:

    fw.write('path,dir,file,ext\n') # タイトル行
    for line in tqdm(resultlist):
        if line.is_file():
            # ファイルのみ書き込み(ディレクトリは書き込まない)
            strpath = str(line)
            strdirname = str(line.parent)
            strfilename = line.name
            strext = line.suffix
            fw.write(strpath+','+strdirname+','+strfilename+','+strext+'\n')

print('処理終了')
