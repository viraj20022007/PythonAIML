def CheckVowel(ch):
    if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        print("Vowel")
    else:
        print("Consonant")


def main():
    Char = input("Enter a character: ")
    CheckVowel(Char)


if __name__ == "__main__":
    main()