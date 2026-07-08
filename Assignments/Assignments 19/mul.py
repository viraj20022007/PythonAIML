Mul = lambda No1,No2:No1*No2


def main():
    Value1 = int(input("Enter a First Number: "))
    Value2 = int(input("Enter a Second Number: "))

    Ret = Mul(Value1,Value2)

    print(f"The Multiplication of {Value1} and {Value2} is : ",Ret)

if __name__ == "__main__":
    main()