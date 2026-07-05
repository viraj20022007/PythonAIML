from functools import reduce

Maximum = lambda No1,No2 : No1 if No1 < No2 else No2

def main():
    Data = [10,40,20,60,30]

    print("Input data :",Data)

    RData = reduce(Maximum,Data)

    print("Maximum element is :",RData)

if __name__ == "__main__":
    main()