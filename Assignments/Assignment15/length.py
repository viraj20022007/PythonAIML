CheckLength = lambda Str : len(Str) > 5

def main():
    Data = ["Apple","Banana","Cat","Orange","Mango"]

    print("Input data :",Data)

    FData = list(filter(CheckLength,Data))

    print("Data after filter :",FData)

if __name__ == "__main__":
    main()