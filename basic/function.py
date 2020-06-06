# 関数(戻り値なし、引数なし)
def func1():
    """
    関数の説明
    """
    print('func1()')

func1()

def func2(a:int) -> int:
    """
    関数2の説明
    Args:
        a(int) : aの説明
    Returns:
        int : 戻り値の説明
    """
    print('func2()')
    return(12)

func2(1)
