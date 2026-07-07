def SumFactors(No):
    Sum = 0

    for i in range(1, No):
        if(No % i == 0):
            Sum = Sum + i

    return Sum

def main():
    Value = int(input("Enter Number : "))

    Ret = SumFactors(Value)

    print("Addition of Factors :", Ret)

if __name__ == "__main__":
    main()