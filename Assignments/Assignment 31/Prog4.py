import schedule
import time
from datetime import datetime

def CreateLog():
    current = datetime.now()

    filename = "MarvellousLog_" + current.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    with open(filename, "w") as file:
        file.write("Log file created successfully.\n")
        file.write("Creation Time : ")
        file.write(current.strftime("%d-%m-%Y %I:%M:%S %p"))

    print("Log file created :", filename)

def main():
    print("Scheduler Started...")

    schedule.every(10).minutes.do(CreateLog)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()