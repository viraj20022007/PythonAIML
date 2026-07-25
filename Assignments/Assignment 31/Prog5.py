import os
import schedule
import time
from datetime import datetime

Directory = input("Enter Directory Path : ")

def CountFiles():
    if not os.path.isdir(Directory):
        print("Invalid Directory")
        return

    count = 0

    for item in os.listdir(Directory):
        if os.path.isfile(os.path.join(Directory, item)):
            count += 1

    current = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    with open("DirectoryCountLog.txt", "a") as file:
        file.write("Directory : " + Directory + "\n")
        file.write("Number of Files : " + str(count) + "\n")
        file.write("Date and Time : " + current + "\n")
        file.write("-" * 40 + "\n")

    print("Files :", count)

def main():
    print("Directory Monitor Started...")

    CountFiles()

    schedule.every(5).minutes.do(CountFiles)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()