def Sum(Value):
    Total = 0

    for i in range(1, Value + 1):
        Total = Total + i

    return Total


def main():
    No = int(input("Enter a Number: "))

    Ret = Sum(No)
    print("Sum of first", No, "numbers is:", Ret)

if __name__ == "__main__":
    main()