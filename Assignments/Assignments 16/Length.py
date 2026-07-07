def NameLength(Name):
    return len(Name)

def main():
    Value = input("Enter Name : ")

    Ret = NameLength(Value)

    print("Length of Name is :", Ret)

if __name__ == "__main__":
    main()