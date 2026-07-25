def CountWords(filename):
    file = open(filename, "r")

    count = 0

    for line in file:
        words = line.split()
        count = count + len(words)

    file.close()

    print("Total number of words:", count)


def main():
    name = input("Enter file name: ")
    CountWords(name)


if __name__ == "__main__":
    main()