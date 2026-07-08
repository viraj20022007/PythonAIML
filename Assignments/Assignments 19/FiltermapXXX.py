from functools import reduce

def CheckPrime(No):
    if No < 2:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True

FilterX = lambda No : CheckPrime(No)
MapX = lambda No : No * 2
ReduceX = lambda A, B : A if A > B else B

def main():
    Data = [2, 70, 11, 10, 17, 23, 31, 77]

    print("Input List :", Data)

    FData = list(filter(FilterX, Data))
    print("List after filter :", FData)

    MData = list(map(MapX, FData))
    print("List after map :", MData)

    Ret = reduce(ReduceX, MData)
    print("Output of reduce :", Ret)

if __name__ == "__main__":
    main()