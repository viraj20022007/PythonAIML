import os
from multiprocessing import Pool

def Factorial(No):
    Fact = 1

    for i in range(1, No + 1):
        Fact = Fact * i

    print("Process ID :", os.getpid())
    print("Input Number :", No)
    print("Factorial :", Fact)
    print("------------------------")

    return Fact

def main():
    Data = [10, 15, 20, 25]

    p = Pool()

    p.map(Factorial, Data)

    p.close()
    p.join()

if __name__ == "__main__":
    main()