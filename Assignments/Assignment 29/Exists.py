import os

def CheckFile(filename):
    if os.path.exists(filename):
        print("File exists.")
    else:
        print("File does not exist.")

def main():
    name = input("Enter file name: ")
    CheckFile(name)

if __name__ == "__main__":
    main()