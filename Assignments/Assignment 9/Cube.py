def Cube(Value):
    return Value*Value*Value

def main():
    No=int(input("Enter a Number : "))

    Ret = Cube(No)
    print("cube of Number is :",Ret)

if __name__=="__main__":
    main()
