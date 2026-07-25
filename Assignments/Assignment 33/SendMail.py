import smtplib
from email.message import EmailMessage
import os

def SendMail(SenderEmail, AppPassword, ReceiverEmail, FileName):
    try:
        msg = EmailMessage()

        msg["Subject"] = "Duplicate File Removal Log"
        msg["From"] = SenderEmail
        msg["To"] = ReceiverEmail

        msg.set_content("Hello,\n\nPlease find the attached Duplicate File Removal Log.\n\nThank You.")

        with open(FileName, "rb") as f:
            FileData = f.read()
            File_Name = os.path.basename(FileName)

        msg.add_attachment(FileData,
                           maintype="application",
                           subtype="octet-stream",
                           filename=File_Name)

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(SenderEmail, AppPassword)
        server.send_message(msg)

        server.quit()

        print("Mail sent successfully...")

    except Exception as e:
        print("Unable to send mail")
        print(e)