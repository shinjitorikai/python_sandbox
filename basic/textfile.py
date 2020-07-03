from enum import Enum,auto

class AccessMode(Enum):
    READ_ONLY = auto() # 読み込みのみ
    WRITE_OVERWRITE = auto() # ファイルがなければ新規作成、あれば上書き
    WRITE_APPEND = auto()

def textfile_read_str(filepath):
    """
    テキストファイル読み込み(1行ずつ)
    Args:
        filepath : テキストファイルのパス
    Returns:
        テキストファイル全体を読み込んだ文字列
    """
    data = ''
    with open(filepath,mode='r') as f:
        #print(type(f)) # <class '_io.TextIOWrapper'>
        for line in f:
            data += line
    return data

def textfile_read_list(filepath):
    """
    テキストファイル読み込み(リスト)
    Args:
        filepath : テキストファイルのパス
    Returns:
        テキストファイル全体を読み込んだリスト
    """
    with open(filepath,mode='r') as f:
        data = f.readlines()
    return data

def textfile_write_str(filepath,data,wmode):
    """
    テキストファイル書き込み(文字列)
    Args:
        filepath : テキストファイルのパス
        data : テキストファイルに書き出したい文字列
        wmode : 書き込みモード(AccessMode.WRITE_OVERWRITEまたはAccessMode.WRITE_APPEND)
    """
    write_mode = 'w'
    if wmode == AccessMode.WRITE_OVERWRITE:
        pass
    else:
        write_mode = 'a'
    with open(filepath,mode=write_mode) as f:
        f.write(data)

def textfile_write_list(filepath,data,wmode):
    """
    テキストファイル書き込み(リスト)
    (ファイルがなければ新規作成、あれば上書き)
    Args:
        filepath : テキストファイルのパス
        data : テキストファイルに書き出したいリスト
        wmode : 書き込みモード(AccessMode.WRITE_OVERWRITEまたはAccessMode.WRITE_APPEND)
    """
    write_mode = 'w'
    if wmode == AccessMode.WRITE_OVERWRITE:
        pass
    else:
        write_mode = 'a'
    with open(filepath,mode=write_mode) as f:
        f.writelines(data)


filepath = './TestText.txt'
result = textfile_read_str(filepath)
#result = textfile_read_list(filepath)
print(result)

filepath2 = './Temp.txt'
writedata = 'testテスト試験\nABC123'
#textfile_write_str(filepath2,writedata,AccessMode.WRITE_OVERWRITE)
#textfile_write_str(filepath2,writedata,AccessMode.WRITE_APPEND)
writedata2 = ['test\n','テスト\n','試験\n','DEF\n','456\n']
#textfile_write_list(filepath2,writedata2,AccessMode.WRITE_OVERWRITE)
#textfile_write_list(filepath2,writedata2,AccessMode.WRITE_APPEND)
