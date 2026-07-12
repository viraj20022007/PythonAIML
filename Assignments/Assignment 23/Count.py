from multiprocessing import Pool
import os

def CountEven(No):
    Count = 0

    for i in range(2, No + 1):
        if(i % 2 == 0):
            Count = Count + 1

    print("Process ID :", os.getpid())
    print("Input Number :", No)
    print("Even Number Count :", Count)
    print("--------------------------")

    return Count

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    p = Pool()

    p.map(CountEven, Data)

    p.close()
    p.join()

if __name__ == "__main__":
    main()