def Chkdivi(Value):
    if (Value % 3 == 0) and (Value % 5 == 0):
        print("Yes, it is divisible by 3 and 5")
    else:
        print("No,it is not divisible by 3 and 5")


def main():
    No=int(input("Enter a Number : "))

    Chkdivi(No)

if __name__=="__main__":
    main()
