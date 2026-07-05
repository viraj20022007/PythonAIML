CheckOdd = lambda No : (No%2 != 0)  


def main():
    Value = int(input("Enter a number : "))

    Ret = CheckOdd(Value)  

    if(Ret == True):
        print("Its odd number")
    else:
        print("Its even number")

if __name__ == "__main__":
    main()