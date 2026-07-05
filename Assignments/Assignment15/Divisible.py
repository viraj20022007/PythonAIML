CheckDivisible = lambda No : No % 3 == 0 and No % 5 == 0

def main():
    Data = [10,15,20,30,45,50,60]

    print("Input data :",Data)

    FData = list(filter(CheckDivisible,Data))

    print("Data after filter :",FData)

if __name__ == "__main__":
    main()