import os
import schedule
import time
from datetime import datetime

directory = input("Enter Directory Path : ")

def DeleteEmptyFiles():

    if not os.path.isdir(directory):
        print("Invalid Directory")
        return

    logfile = "DeletedFilesLog.txt"

    with open(logfile, "a") as log:

        log.write("\n")
        log.write("Deleted On : " +
                  datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")

        for folder, subfolders, files in os.walk(directory):

            for file in files:

                filepath = os.path.join(folder, file)

                try:

                    if os.path.getsize(filepath) == 0:

                        os.remove(filepath)

                        print("Deleted :", filepath)

                        log.write(filepath + "\n")

                except Exception as e:

                    print("Error :", e)


def main():

    print("Empty File Cleaner Started...")

    DeleteEmptyFiles()

    schedule.every(1).hours.do(DeleteEmptyFiles)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()