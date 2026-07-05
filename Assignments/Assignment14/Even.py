CheckEven = lambda No : (No%2 == 0)  


def main():
    Value = int(input("Enter a number : "))

    Ret = CheckEven(Value)  #Ret =(Value % 2 == 0)

    if(Ret == True):
        print("Its even number")
    else:
        print("Its odd number")

if __name__ == "__main__":
    main()