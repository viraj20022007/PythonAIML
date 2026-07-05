CheckSquare = lambda No : No*No


def main():
    Value = int(input("Enter a number : "))

    Ret = CheckSquare(Value)  

    print("sqaure of number is : ",Ret)

if __name__ == "__main__":
    main()