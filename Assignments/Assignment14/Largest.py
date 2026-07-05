CheckLar = lambda No1, No2, No3: max(No1, No2, No3)

def main():
    Value1 = int(input("Enter first number: "))
    Value2 = int(input("Enter second number: "))
    Value3 = int(input("Enter third number: "))

    Ret = CheckLar(Value1, Value2, Value3)

    print("Largest number is:", Ret)

if __name__ == "__main__":
    main()