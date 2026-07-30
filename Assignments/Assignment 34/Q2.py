import psutil
import sys

def ProcessScan(ProcessName):

    Flag = False

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=["pid", "name", "username"])

            if(info["name"].lower() == ProcessName.lower()):
                Flag = True

                print("-" * 50)
                print("Process Found")
                print("PID       :", info["pid"])
                print("Name      :", info["name"])
                print("Username  :", info["username"])
                print("-" * 50)

        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            pass

    if Flag == False:
        print("Process is not running.")

def main():

    Border = "-" * 60

    print(Border)
    print("Marvellous Infosystems : Process Information")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script displays information of a running process.")
            print("Provide the process name as command line argument.")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage :")
            print("python ProcInfo.py Process_Name")
            print("Example :")
            print("python ProcInfo.py notepad.exe")

        else:
            ProcessName = sys.argv[1]
            ProcessScan(ProcessName)

    else:
        print("Invalid number of arguments.")
        print("Use --h for help")
        print("Use --u for usage")

    print(Border)
    print("Thank you for using our automation system")
    print(Border)

if __name__ == "__main__":
    main()