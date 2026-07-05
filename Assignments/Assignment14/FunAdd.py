CheckAdd = lambda No1,No2 : (No1+No2)  


def main():
    Value1 = int(input("Enter a first number : "))
    Value2 = int(input("Enter a second number : "))

    Ret = CheckAdd(Value1,Value2)  

    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()