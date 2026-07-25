import schedule
import time
from datetime import datetime

def WriteFile():
    with open("Marvellous.txt", "a") as file:
        current = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
        file.write("Task executed at : " + current + "\n")

    print("Task executed at :", current)

def main():
    print("Scheduler Started...")

    schedule.every(5).minutes.do(WriteFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()