from functools import reduce

Addition = lambda No1,No2 : No1 + No2

def main():
    Data = [10,20,30,40,50]

    print("Input data :",Data)

    RData = reduce(Addition,Data)

    print("Addition is :",RData)

if __name__ == "__main__":
    main()