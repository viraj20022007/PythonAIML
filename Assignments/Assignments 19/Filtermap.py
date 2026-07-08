from functools import reduce

def CheckNo(No):
    if(No >= 70) and (No <= 90):
        return True
    else:
        return False

def Increment(No):
    return No + 10

def Product(A, B):
    return A * B

def main():
    Data = [4,34,36,76,68,24,89,23,86,90,45,70]

    print("Input data is :", Data)

    FData = list(filter(CheckNo, Data))
    print("Data after filter :", FData)

    MData = list(map(Increment, FData))
    print("Data after map :", MData)

    Ret = reduce(Product, MData)
    print("Output of reduce :", Ret)

if __name__ == "__main__":
    main()