def Frequency(Data, No):
    Count = 0

    for i in Data:
        if(i == No):
            Count = Count + 1

    return Count

def main():
    Size = int(input("Enter number of elements : "))

    Data = []

    print("Enter elements :")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Search = int(input("Enter number to search : "))

    Ret = Frequency(Data, Search)

    print("Frequency is :", Ret)

if __name__ == "__main__":
    main()