def CheckPrime(Value):
    if Value <= 1:
        return False

    for i in range(2, Value):
        if Value % i == 0:
            return False

    return True


def main():
    No = int(input("Enter a Number: "))

    if CheckPrime(No):
        print(No, "is a Prime Number")
    else:
        print(No, "is not a Prime Number")


if __name__ == "__main__":
    main()