def Binary(No):
    return bin(No)[2:]


def main():
    Value = int(input("Enter a number: "))

    Ret = Binary(Value)
    print("Binary number is:", Ret)


if __name__ == "__main__":
    main()