import psutil
import sys
import os
import time
import smtplib
from email.message import EmailMessage

def ProcessScan():

    listprocess = []

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=["pid","name","username"])
            listprocess.append(info)

        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            pass

    return listprocess


def CreateLog(FolderName):

    Border = "-" * 60

    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName, "Marvellous_%s.log" % timestamp)

    fobj = open(FileName, "w", encoding="utf-8")

    fobj.write(Border + "\n")
    fobj.write("Marvellous Infosystems Process Log\n")
    fobj.write("Created on : " + timestamp + "\n")
    fobj.write(Border + "\n\n")

    Data = ProcessScan()

    for info in Data:
        fobj.write("PID : %s\n" % info["pid"])
        fobj.write("Name : %s\n" % info["name"])
        fobj.write("Username : %s\n" % info["username"])
        fobj.write(Border + "\n")

    fobj.close()

    return FileName


def SendMail(FileName, ReceiverMail):

    SenderMail = "virajskond@gmail.com"
    Password = "gkqebtmohhkupbei"

    msg = EmailMessage()

    msg["Subject"] = "Process Log File"
    msg["From"] = SenderMail
    msg["To"] = ReceiverMail

    msg.set_content("Please find the attached process log file.")

    with open(FileName, "rb") as f:
        data = f.read()

    msg.add_attachment(data,
                       maintype="application",
                       subtype="octet-stream",
                       filename=os.path.basename(FileName))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(SenderMail, Password)
    server.send_message(msg)
    server.quit()

    print("Mail sent successfully.")


def main():

    Border = "-" * 60

    print(Border)
    print("Marvellous Infosystems : Process Logger")
    print(Border)

    if(len(sys.argv) == 3):

        FolderName = sys.argv[1]
        ReceiverMail = sys.argv[2]

        FileName = CreateLog(FolderName)
        SendMail(FileName, ReceiverMail)

    else:
        print("Usage :")
        print("python Demo EmailID")

    print(Border)
    print("Thank you for using our automation system")
    print(Border)


if __name__ == "__main__":
    main()