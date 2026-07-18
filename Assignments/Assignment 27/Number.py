class Numbers:

    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False

        return True

    def ChkPerfect(self):
        Sum = 0

        for i in range(1, self.Value):
            if self.Value % i == 0:
                Sum = Sum + i

        if Sum == self.Value:
            return True
        else:
            return False

    def Factors(self):
        print("Factors are :", end=" ")

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")

        print()

    def SumFactors(self):
        Sum = 0

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                Sum = Sum + i

        return Sum


obj1 = Numbers(28)

print("Number :", obj1.Value)

if obj1.ChkPrime():
    print("Prime Number")
else:
    print("Not Prime Number")

if obj1.ChkPerfect():
    print("Perfect Number")
else:
    print("Not Perfect Number")

obj1.Factors()

print("Sum of Factors :", obj1.SumFactors())

print("-----------------------------")

obj2 = Numbers(13)

print("Number :", obj2.Value)

if obj2.ChkPrime():
    print("Prime Number")
else:
    print("Not Prime Number")

if obj2.ChkPerfect():
    print("Perfect Number")
else:
    print("Not Perfect Number")

obj2.Factors()

print("Sum of Factors :", obj2.SumFactors())