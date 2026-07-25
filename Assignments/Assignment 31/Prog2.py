import schedule
import time

def DisplayMessage(message):
    print(message)

message = input("Enter message: ")

print("Scheduler Started...")

schedule.every(5).seconds.do(DisplayMessage, message)

while True:
    schedule.run_pending()
    time.sleep(1)