from multiprocessing import Pool
import time

def SumPower5(No):
    Sum = 0

    for i in range(1, No + 1):
        Sum = Sum + (i ** 5)

    return Sum

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    print("Input :", Data)

    Start = time.time()

    p = Pool()

    Result = p.map(SumPower5, Data)

    p.close()
    p.join()

    End = time.time()

    print("Output :")
    for Value in Result:
        print(Value)

    print("Execution Time :", End - Start)

if __name__ == "__main__":
    main()