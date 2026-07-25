import schedule
import time
import os

filename = input("Enter file name: ")

def ReadFile():

    if not os.path.exists(filename):
        print("File does not exist.")
        return

    try:
        with open(filename, "r") as file:

            data = file.read()

            if len(data.strip()) == 0:
                print("File is empty.")
            else:
                print("\nFile Contents:")
                print(data)

    except PermissionError:
        print("Permission denied.")

    except OSError:
        print("File cannot be opened.")

def main():
    print("File Reader Started...")

    ReadFile()

    schedule.every(1).minutes.do(ReadFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()