def DisplayGrade(Marks):

    if Marks >= 75:
        return "Distinction"
    elif Marks >= 60:
        return "First Class"
    elif Marks >= 50:
        return "Second Class"
    else:
        return "Fail"


def main():
    Value = int(input("Enter Marks: "))

    Ret = DisplayGrade(Value)

    print("Grade is:", Ret)


if __name__ == "__main__":
    main()