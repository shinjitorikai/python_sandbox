import os
import glob

# 設定値
target_path = '/Users/torikai/OneDrive/working/comute_20210320/AI-SCHOLAR/202104/*.pdf'
replace_before = ' | AI-SCHOLAR | AI：(人工知能)論文・技術情報メディア'
replace_after = '_AI-SCHOLAR'

# ファイルリストを取得
files = glob.glob(target_path)
for filename in files:
    newfilename = filename.replace(replace_before, replace_after)
    print(newfilename)

    # ファイル名変更
    os.rename(filename, newfilename)
