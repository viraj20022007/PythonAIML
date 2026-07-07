def Minimum(Data):
    Min = Data[0]

    for i in Data:
        if(i < Min):
            Min = i

    return Min

def main():
    Size = int(input("Enter number of elements : "))

    Data = []

    print("Enter elements :")

    for i in range(Size):
        No = int(input())
        Data.append(No)

    Ret = Minimum(Data)

    print("Minimum number is :", Ret)

if __name__ == "__main__":
    main()