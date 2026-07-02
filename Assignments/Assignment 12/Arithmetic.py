def Arithmetic(No1, No2):
    print("Addition =", No1 + No2)
    print("Subtraction =", No1 - No2)
    print("Multiplication =", No1 * No2)

    if No2 != 0:
        print("Division =", No1 / No2)
    else:
        print("Division is not possible")


def main():
    Value1 = int(input("Enter first number: "))
    Value2 = int(input("Enter second number: "))

    Arithmetic(Value1, Value2)


if __name__ == "__main__":
    main()