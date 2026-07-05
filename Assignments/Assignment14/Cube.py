CheckCube = lambda No : No**3


def main():
    Value = int(input("Enter a number : "))

    Ret = CheckCube(Value)  

    print("Cube of number is : ",Ret)

if __name__ == "__main__":
    main()