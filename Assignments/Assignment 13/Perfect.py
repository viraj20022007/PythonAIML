def Perfect(Num):
    Sum = 0

    for i in range(1, Num):
        if Num % i == 0:
            Sum = Sum + i

    if Sum == Num:
        return True
    else:
        return False


def main():
    No = int(input("Enter a number: "))

    Ret = Perfect(No)

    if Ret == True:
        print("It is a perfect number")
    else:
        print("It is not a perfect number")


if __name__ == "__main__":
    main()