import sys

def CopyFile(source):
    file1 = open(source, "r")
    data = file1.read()
    file1.close()

    file2 = open("Demo.txt", "w")
    file2.write(data)
    file2.close()

    print("Contents copied successfully.")

def main():
    if len(sys.argv) != 2:
        print("Usage : python CopyFile.py <filename>")
        return

    CopyFile(sys.argv[1])

if __name__ == "__main__":
    main()