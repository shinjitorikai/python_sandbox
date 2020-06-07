class AAA:
    def __init__(self): # コンストラクタ
        print('AAA Constructor')

    def method1(self):
        print('AAA.method1()')

    def method2(self,a,b):
        print('method2 - arg1 : ' + str(a) + ', arg2 : ' + str(b))
    
    def method3(self,a,b):
        return a+b

a = AAA() # インスタンス生成
a.method1()
a.method2(1,2)
a.method3(2,3)

# instance/class variable
class SampleClass_WithVariable:
  classvar_x = 0
  def __init__(self, x):
    self.x = x
    SampleClass_WithVariable.classvar_x += 1
    
  def printInstanceVar(self):
    print('instance variable : ' + str(self.x))
  
  def printClassVar(self):
    print('class variable : ' + str(SampleClass_WithVariable.classvar_x))

sampleClassWithVariable1 = SampleClass_WithVariable(3)
sampleClassWithVariable1.printInstanceVar()
sampleClassWithVariable1.printClassVar()

sampleClassWithVariable2 = SampleClass_WithVariable(5)
sampleClassWithVariable2.printInstanceVar()
sampleClassWithVariable2.printClassVar()

# inheritance
class BaseClass():
  def __init__(self):
    print('base class constructor')

class SubClass(BaseClass):
  def __init__(self):
    super().__init__()
    print('sub class constructor')

subClass = SubClass()
