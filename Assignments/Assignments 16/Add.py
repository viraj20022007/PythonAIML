def Add(No1,No2):
    Sum = No1 + No2
    return Sum
    

def main():
    Value1 = int(input("Enter a first Number : "))
    Value2 = int(input("Enter a second Number : "))

    Ret = Add(Value1,Value2)

    print(f"Addition of {Value1} and {Value2} is : ",Ret)

if __name__ == "__main__":
    main()