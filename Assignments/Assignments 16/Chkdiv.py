def ChkNum(No):
    if(No % 5 == 0):
        return True
    else:
        return False

def main():
    Value = int(input("Enter a Number : "))

    Ret = ChkNum(Value)

    print(Ret)

if __name__ == "__main__":
    main()