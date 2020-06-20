# Requirement
# pip install openpyxl

import openpyxl

# ブックの新規作成
xlbook = openpyxl.Workbook()

# シートの取得
xlsheet = xlbook.active

# セルに値を書き込み
xlcell = xlsheet['B3']
xlcell.value = 'テスト試験123'

# ブックを保存
xlbook.save('./output.xlsx')
