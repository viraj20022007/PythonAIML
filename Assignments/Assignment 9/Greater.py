def Chkgreater(Value1,Value2):

    if Value1 > Value2:
        return Value1
    else:
        return Value2


def main():
    No1=int(input("Enter First Number : "))

    No2=int(input("Enter Second Number : "))

    Ret = Chkgreater(No1,No2)
    print("Greater value is : ",Ret)

if  __name__=="__main__":
    main()