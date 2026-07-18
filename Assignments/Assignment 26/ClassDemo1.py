class Demo:
    Value = 10      # Class variable

    def __init__(self, A, B):
        self.No1 = A
        self.No2 = B

    def fun(self):
        print(self.No1)
        print(self.No2)
        print(Demo.Value)

    def gun(self):
        print(self.No1)
        print(self.No2)
        print(Demo.Value)

obj1 = Demo(11, 21)
obj2 = Demo(51, 101)

obj1.fun()
obj2.fun()
obj1.gun()
obj2.gun()