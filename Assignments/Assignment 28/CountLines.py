def CountLines(filename):
    count = 0

    file = open(filename, "r")

    for line in file:
        count += 1

    file.close()

    print("Total number of lines:", count)


def main():
    name = input("Enter file name: ")
    CountLines(name)


if __name__ == "__main__":
    main()