def Frequency(filename, word):
    file = open(filename, "r")

    data = file.read()

    file.close()

    words = data.split()

    count = words.count(word)

    print(word, "appears", count, "times.")

def main():
    name = input("Enter file name: ")
    word = input("Enter word: ")

    Frequency(name, word)

if __name__ == "__main__":
    main()