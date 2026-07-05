CheckDiv = lambda No : (No%5 == 0)  


def main():
    Value = int(input("Enter a number : "))

    Ret = CheckDiv(Value)  

    if(Ret == True):
        print("Yes it is divisible by 5")
    else:
        print("No it is not divisible by 5")

if __name__ == "__main__":
    main()