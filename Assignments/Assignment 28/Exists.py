def SearchWord(filename, word):
    file = open(filename, "r")

    data = file.read()

    file.close()

    if word in data:
        print(word, "is present in the file.")
    else:
        print(word, "is not present in the file.")


def main():
    name = input("Enter file name: ")
    word = input("Enter word to search: ")

    SearchWord(name, word)


if __name__ == "__main__":
    main()