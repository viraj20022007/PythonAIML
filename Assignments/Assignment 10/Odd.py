def Odd(Value):

    for i in range(1, Value+1):
        if(i % 2 != 0):
            print("Odd no is : ",i)


def main():
    No = int(input("Enter a Number: "))

    Odd(No)

if __name__ == "__main__":
    main()