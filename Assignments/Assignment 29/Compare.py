import sys

def Compare(file1, file2):
    f1 = open(file1, "r")
    f2 = open(file2, "r")

    data1 = f1.read()
    data2 = f2.read()

    f1.close()
    f2.close()

    if data1 == data2:
        print("Success")
    else:
        print("Failure")

def main():
    if len(sys.argv) != 3:
        print("Usage : python Compare.py File1 File2")
        return

    Compare(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()