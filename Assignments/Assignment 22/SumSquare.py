from multiprocessing import Pool

def SumSquare(No):
    return (No * (No + 1) * (2 * No + 1)) // 6

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    print("Input :", Data)

    p = Pool()

    Result = p.map(SumSquare, Data)

    p.close()
    p.join()

    print("Output :", Result)

if __name__ == "__main__":
    main()