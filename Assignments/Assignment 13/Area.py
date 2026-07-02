def Area(Len,Wid):

    return Len*Wid
        

def main():
    Length = int(input("enter a length : "))
    Width = int(input("enter a width : "))

    Ret = Area(Length,Width)
    print("Area of rectangle is : ",Ret)

if __name__ == "__main__":
    main()