Power = lambda No:No**2


def main():
    Value = int(input("Enter a Number: "))

    Ret = Power(Value)

    print(f"The Power of {Value} is : ",Ret)

if __name__ == "__main__":
    main()