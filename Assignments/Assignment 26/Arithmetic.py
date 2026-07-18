class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter First Number : "))
        self.Value2 = int(input("Enter Second Number : "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if self.Value2 == 0:
            return "Division by zero is not possible"
        return self.Value1 / self.Value2


obj1 = Arithmetic()

obj1.Accept()

print("Addition :", obj1.Addition())
print("Subtraction :", obj1.Subtraction())
print("Multiplication :", obj1.Multiplication())
print("Division :", obj1.Division())    