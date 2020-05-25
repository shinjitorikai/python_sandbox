class AAA:
    def __init__(self): # コンストラクタ
        print('AAA Constructor')

    def method1(self):
        print('AAA.method1()')

a = AAA() # インスタンス生成
a.method1()
