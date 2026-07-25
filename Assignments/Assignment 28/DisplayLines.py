def DisplayLines(filename):
    file = open(filename, "r")

    count = 0

    for line in file:
        print(line)
        count = count + 1

    file.close()



def main():
    name = input("Enter file name: ")
    DisplayLines(name)


if __name__ == "__main__":
    main()