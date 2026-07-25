import os
import schedule
import time
from datetime import datetime

directory = input("Enter Directory Path: ")

def ScanDirectory():

    if not os.path.isdir(directory):
        print("Invalid Directory")
        return

    files = 0
    folders = 0

    for item in os.listdir(directory):
        path = os.path.join(directory, item)

        if os.path.isfile(path):
            files += 1
        elif os.path.isdir(path):
            folders += 1

    current = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    print("\nDirectory Scanned :", directory)
    print("Total Files :", files)
    print("Total Subdirectories :", folders)
    print("Scan Time :", current)

print("Scheduler Started...")

ScanDirectory()

schedule.every(1).minutes.do(ScanDirectory)

while True:
    schedule.run_pending()
    time.sleep(1)