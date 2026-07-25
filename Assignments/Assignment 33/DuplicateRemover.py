import sys
import os
import schedule
import time
from datetime import datetime

from SendMail import SendMail
from Marvellous import DeleteDuplicate


def CreateDirectory():

    if os.path.exists("Marvellous") == False:
        os.mkdir("Marvellous")


def CreateLogFile():

    CurrentTime = datetime.now()

    FileName = "DuplicateRemovalLog_" + CurrentTime.strftime("%d_%m_%Y_%H_%M_%S") + ".log"

    FilePath = os.path.join("Marvellous", FileName)

    fobj = open(FilePath,"w")

    fobj.write("Duplicate File Removal Log\n")
    fobj.write("-----------------------------------------\n")
    fobj.write("Log Creation Time : ")
    fobj.write(CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p"))
    fobj.write("\n\n")

    fobj.close()

    return FilePath


def Process(DirectoryName, ReceiverEmail):

    CreateDirectory()

    LogFile = CreateLogFile()

    DeleteDuplicate(DirectoryName, LogFile)

    print("Log File Created :", LogFile)

    SenderEmail = "virajskond@gmail.com"

    AppPassword = "wocixdzjxbolgfzk"

    SendMail(SenderEmail,
             AppPassword,
             ReceiverEmail,
             LogFile)


def main():

    if(len(sys.argv) != 4):
        print("Usage : python DuplicateRemover.py DirectoryName TimeInterval ReceiverEmail")
        return

    DirectoryName = sys.argv[1]

    Interval = int(sys.argv[2])

    ReceiverEmail = sys.argv[3]

    Process(DirectoryName, ReceiverEmail)

    schedule.every(Interval).minutes.do(Process,
                                        DirectoryName,
                                        ReceiverEmail)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()