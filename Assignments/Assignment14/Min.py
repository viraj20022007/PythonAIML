CheckMin = lambda No1, No2: No1 < No2

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Ret = CheckMin(Value1, Value2)

    if Ret == True:
        print(Value1, "is minimum")
    else:
        print(Value2, "is minimum")

if __name__ == "__main__":
    main()