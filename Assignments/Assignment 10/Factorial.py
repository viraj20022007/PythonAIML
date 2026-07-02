def Factorial(Value):
    mul = 1

    for i in range(1, Value + 1):
        mul = mul * i

    return mul


def main():
    No = int(input("Enter a Number: "))

    Ret = Factorial(No)
    print("Factorial of", No, "is:", Ret)

if __name__ == "__main__":
    main()