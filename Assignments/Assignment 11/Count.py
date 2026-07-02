def CountDigits(Value):
    Count = 0

    while Value > 0:
        Count = Count + 1
        Value = Value // 10

    return Count


def main():
    No = int(input("Enter a Number: "))

    if No == 0:
        print("Number of digits is: 1")
    else:
        Ret = CountDigits((No))
        print("Number of digits is:", Ret)


if __name__ == "__main__":
    main()