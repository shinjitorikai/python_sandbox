import pandas as pd
from tqdm import tqdm
from pathlib import Path
import os

# 設定値
TARGET_DIR = r'/Users/torikai/Documents/sandbox/python_sandbox'
SEARCH_PATTERN = '*'
ISRECURSIVE = True
OUTPUT_FILENAME = r'./filesystem/output.csv'

def getfilelist(targetdir,pattern,isrecursive):
    p = Path(targetdir)
    if isrecursive == True:
        search_pattern = '**/' + pattern
    else:
        search_pattern = pattern    
    filelist = [str(filename) for filename in list(p.glob(search_pattern))]
    return filelist

def getfilelist_df(targetdir,pattern,isrecursive):
    p = Path(targetdir)
    if isrecursive == True:
        search_pattern = '**/' + pattern
    else:
        search_pattern = pattern    
    path_list = [str(filename) for filename in list(p.glob(search_pattern))]
    fname_list = [os.path.basename(s) for s in path_list]
    df = pd.DataFrame({'Path':path_list,'FileName':fname_list})
    return df

def main():
    # ファイル/フォルダを取得
    print('ファイル/フォルダを取得...')
    filelist = getfilelist(TARGET_DIR, SEARCH_PATTERN, ISRECURSIVE)

    # 結果をファイルに出力
    print('結果をファイルに出力...')
    file_num = 0
    #with open(OUTPUT_FILENAME,mode='w',encoding='utf-8') as fw: # utf-8だとExcelで開いたときに文字化け
    with open(OUTPUT_FILENAME,mode='w') as fw:

        fw.write('path,dir,file,ext,size_byte\n') # タイトル行
        for line in tqdm(filelist):
            if os.path.isfile(line):
                # ファイルのみ書き込み(ディレクトリは書き込まない)
                strpath = line
                strdirname = os.path.dirname(line)
                strfilename = os.path.basename(line)
                _,strext = os.path.splitext(line)
                strfilesize_byte = str(os.path.getsize(line))
                fw.write(strpath+','+strdirname+','+strfilename+','+strext+','+strfilesize_byte+'\n')
                file_num += 1

    print('file_num : ',file_num)
    print('処理終了')

if __name__ == '__main__':
    main()
