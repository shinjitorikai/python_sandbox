# デコレーター定義
def deco(func):
    def wrapper(*args,**kwargs):
        print('/////')
        func(*args,**kwargs)
        print('-----')
    return wrapper

@deco
def test():
    print('Test')

test()
