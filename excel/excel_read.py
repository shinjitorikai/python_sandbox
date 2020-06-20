# Requirement
# pip install openpyxl

import openpyxl

# ブックのオープン
xlbook = openpyxl.load_workbook('./output.xlsx')

# シートの取得
xlsheets = xlbook.get_sheet_names()
print('xlsheets : ',xlsheets)

# セルの値を読み込み
xlsheet = xlbook._sheets[0]
xlcell = xlsheet['B3']
print('B3 : ',xlcell.value)
