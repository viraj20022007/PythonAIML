def ChkPrime(No):
    Count = 0

    for i in range(1, No + 1):
        if(No % i == 0):
            Count = Count + 1

    if(Count == 2):
        return True
    else:
        return False

def main():
    Value = int(input("Enter Number : "))

    Ret = ChkPrime(Value)

    if(Ret == True):
        print("It is Prime Number")
    else:
        print("It is Not Prime Number")

if __name__ == "__main__":
    main()