from multiprocessing import Pool

def PrimeCount(No):
    Count = 0

    for i in range(2, No + 1):
        Prime = True

        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                Prime = False
                break

        if Prime:
            Count = Count + 1

    return Count

def main():
    Data = [10000, 20000, 30000, 40000]

    print("Input :", Data)

    p = Pool()

    Result = p.map(PrimeCount, Data)

    p.close()
    p.join()

    for i in range(len(Data)):
        print("Prime count between 1 and", Data[i], "=", Result[i])

if __name__ == "__main__":
    main()  