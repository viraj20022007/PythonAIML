from functools import reduce

def CheckEven(No):
    if(No %2==0):
        return True
    else:
        return False

def Square(No):
    return No**2

def Add(A, B):
    return A + B

def main():
    Data = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

    print("Input data is :", Data)

    FData = list(filter(CheckEven, Data))
    print("Data after filter :", FData)

    MData = list(map(Square, FData))
    print("Data after map :", MData)

    Ret = reduce(Add, MData)
    print("Output of reduce :", Ret)

if __name__ == "__main__":
    main()