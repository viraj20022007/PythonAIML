def ACircle(Rad):
    PI = 3.14
    return  PI*Rad*Rad
        

def main():
    Radius = int(input("enter a Radius : "))

    Ret = ACircle(Radius)
    print("Area of Circle is : ",Ret)

if __name__ == "__main__":
    main()