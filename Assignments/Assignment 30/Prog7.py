import os
import shutil
import schedule
import time
from datetime import datetime

def Backup():
    source = input("Enter source file path : ")
    destination = input("Enter destination folder path : ")

    if not os.path.isfile(source):
        print("Source file not found.")
        return

    if not os.path.exists(destination):
        os.makedirs(destination)

    filename = os.path.basename(source)
    name, ext = os.path.splitext(filename)

    timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

    backupfile = f"{name}_{timestamp}{ext}"

    destinationfile = os.path.join(destination, backupfile)

    shutil.copy2(source, destinationfile)

    logfile = os.path.join(destination, "backup_log.txt")

    with open(logfile, "a") as file:
        file.write(f"Backup completed successfully at {datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}\n")

    print("Backup completed successfully.")
    print("Backup File :", destinationfile)

def main():
    print("Backup Scheduler Started...")

    Backup()

    schedule.every(1).hours.do(Backup)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()