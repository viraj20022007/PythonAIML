Square = lambda No: No * No
Increment = lambda No: No + 1

def main():
    Data = [2, 4, 6, 8, 10]

    print("Input data :", Data)

    SData = list(map(Square, Data))
    print("After Square :", SData)

    MData = list(map(Increment, SData))
    print("After Increment :", MData)

if __name__ == "__main__":
    main()