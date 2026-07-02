def Reverse(Value):
    Rev = 0

    while Value > 0:
        Digit = Value % 10
        Rev = (Rev * 10) + Digit
        Value = Value // 10

    return Rev


def main():
    No = int(input("Enter a Number: "))

    Ret = Reverse(No)
    print("Reverse of number is:", Ret)


if __name__ == "__main__":
    main()  