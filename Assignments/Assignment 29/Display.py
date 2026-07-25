def DisplayLines(filename):
    file = open(filename, "r")
    Data = file.read()

    print(Data)

    file.close()



def main():
    name = input("Enter file name: ")
    DisplayLines(name)


if __name__ == "__main__":
    main()