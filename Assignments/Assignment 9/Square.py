def Square(Value1):
    return Value1*Value1

def main():
    No1=int(input("Enter a Number : "))

    Ret = Square(No1)
    print("Square of Number is : ",Ret)

if __name__=="__main__":
    main()
