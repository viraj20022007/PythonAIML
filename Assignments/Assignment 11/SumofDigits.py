def SumDigits(Value):
    Sum = 0

    Value = abs(Value)      # Handles negative numbers

    while Value > 0:
        Digit = Value % 10
        Sum = Sum + Digit
        Value = Value // 10

    return Sum


def main():
    No = int(input("Enter a Number: "))

    Ret = SumDigits(No)
    print("Sum of digits is:", Ret)


if __name__ == "__main__":
    main()