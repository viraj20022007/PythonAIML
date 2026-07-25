import os
import schedule
import time
from datetime import datetime

filename = input("Enter file name: ")

def FileSizeMonitor():

    if not os.path.exists(filename):
        print("File does not exist.")
        return

    size = os.path.getsize(filename)
    current = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    with open("FileSizeLog.txt", "a") as file:
        file.write("File Path : " + filename + "\n")
        file.write("File Size : " + str(size) + " bytes\n")
        file.write("Date and Time : " + current + "\n")
        file.write("-" * 40 + "\n")

    print("File Size :", size, "bytes")

def main():
    print("Monitoring Started...")

    FileSizeMonitor()

    schedule.every(30).seconds.do(FileSizeMonitor)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()