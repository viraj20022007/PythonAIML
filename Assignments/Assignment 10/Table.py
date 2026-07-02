def Table(Value):
    for i in range(1,11):
        print(f"{Value} x {i} = {Value * i}")
    

def main():
    No=int(input("Enter a Number : "))

    Table(No)

if __name__=="__main__":
    main()
