import MarvellousNum

def ListPrime(Data):
    Sum = 0

    for i in Data:
        if(MarvellousNum.ChkPrime(i) == True):
            Sum = Sum + i

    return Sum

def main():
    Size = int(input("Enter number of elements : "))

    Data = []

    print("Enter elements :")

    for i in range(Size):
        No = int(input())
        Data.append(No)

    Ret = ListPrime(Data)

    print("Addition of prime numbers is :", Ret)

if __name__ == "__main__":
    main()