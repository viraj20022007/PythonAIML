from multiprocessing import Pool
import os

def SumOdd(No):
    Sum = 0

    for i in range(1, No + 1, 2):
        Sum = Sum + i

    print("Process ID :", os.getpid())
    print("Input Number :", No)
    print("Sum of Odd Numbers :", Sum)
    print("--------------------------")

    return Sum

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    p = Pool()

    p.map(SumOdd, Data)

    p.close()
    p.join()

if __name__ == "__main__":
    main()