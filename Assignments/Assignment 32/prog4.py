import os
import shutil
import schedule
import time
from datetime import datetime

source = input("Enter Source Directory : ")
destination = input("Enter Destination Directory : ")

def CopyFiles():

    if not os.path.isdir(source):
        print("Invalid Source Directory")
        return

    if not os.path.isdir(destination):
        print("Invalid Destination Directory")
        return

    logfile = os.path.join(destination, "CopyLog.txt")

    with open(logfile, "a") as log:

        log.write("\n")
        log.write("Copy Time : " +
                  datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")

        for file in os.listdir(source):

            if file.endswith(".txt"):

                src = os.path.join(source, file)
                dest = os.path.join(destination, file)

                try:
                    shutil.copy2(src, dest)

                    print(file, "Copied Successfully")

                    log.write(file + " Copied Successfully\n")

                except Exception as e:

                    print("Unable to copy", file)

                    log.write(file + " Failed : " + str(e) + "\n")


def main():

    print("Copy Scheduler Started...")

    CopyFiles()

    schedule.every(10).minutes.do(CopyFiles)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()