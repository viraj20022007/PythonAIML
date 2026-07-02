def Even(Value):

    for i in range(1, Value+1):
        if(i % 2 == 0):
            print("even no is : ",i)


def main():
    No = int(input("Enter a Number: "))

    Even(No)

if __name__ == "__main__":
    main()