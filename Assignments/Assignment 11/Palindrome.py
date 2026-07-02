def CheckPalindrome(Value):
    Temp = Value
    Rev = 0

    while Value > 0:
        Digit = Value % 10
        Rev = (Rev * 10) + Digit
        Value = Value // 10

    if Temp == Rev:
        return True
    else:
        return False


def main():
    No = int(input("Enter a Number: "))

    if CheckPalindrome(No):
        print("Palindrome")
    else:
        print("Not Palindrome")


if __name__ == "__main__":
    main()