import psutil
import sys
import os
import time
import schedule

def ProcessScan():
    listprocess = []
    for proc in psutil.process_iter():   #iter is used to itrate the process 
        info = proc.as_dict(attrs=["pid","name","username","status"])  #convert into dictionary
        info["CPU_percent"] = proc.cpu_percent(None)
        info["memory_percent"] = proc.memory_percent()

        listprocess.append(info)

    return listprocess

def PlatformSurveilence(FolderName):
    Border = "-"*60

    Ret = False 

    Ret = os.path.exists(FolderName) #to find it exists

    if(Ret == True):
        Ret =os.path.isdir(FolderName) #to check directory is their

        if(Ret == False):   #jr nasel tr false
            print("Unable proceed as Directory name is exisiting but its not a directory")
            return
    else:
        os.mkdir(FolderName) #if file is not available, it creates by mkdir
        print("Directory for the logfile gets created succesfully...")

    #Logfile creation starts
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S") #time in string(year,month,date_hrs,min,sec)
    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp) #%s fpr string 
    #file gets created
    fobj = open(FileName,"w")
    print(f"Logfile gets successfully created by name {FileName}")



    fobj.write(Border+"\n")
    fobj.write("----------Marvellous platform Surveilence System----------\n")    
    fobj.write("Logfile gets created as :"+timestamp+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("----------------System Report------------\n")

    #CPU Information
    fobj.write("Number of Active CPU Cores : %s\n" %psutil.cpu_count())
    fobj.write("CPU USAGE : %s %%\n" %psutil.cpu_percent())
    fobj.write(Border+"\n")

    #RAM Information
    memory = psutil.virtual_memory()
    fobj.write("RAM USAGE : %s %%\n" %memory.percent)
    fobj.write("Total RAM Available : %s \n" %memory.total)
    fobj.write(Border+"\n")

    #Network usage
    netobj = psutil.net_io_counters()
    fobj.write("Network Usage Report\n")
    fobj.write("Sent: %.2f MB\n"%(netobj.bytes_sent / (1024 * 1024)))
    fobj.write("Receive: %.2f MB\n"%(netobj.bytes_recv / (1024 * 1024)))
    fobj.write(Border+"\n")

    #process log
    Data = ProcessScan()
    for info in Data:
        #fobj.write(f"{info}\n")
        fobj.write("PID : %s \n" %info.get("pid"))
        fobj.write("Name : %s \n" %info.get("name"))
        fobj.write("Username : %s \n" %info.get("username"))
        fobj.write("status : %s \n" %info.get("status"))
        fobj.write("CPU usage : %.2f\n" % info.get("CPU_percent"))
        fobj.write("Ram percent : %.2f \n" %info.get("memory_percent"))
        fobj.write(Border+"\n")


    fobj.write(Border+"\n")
    fobj.write("----------------End of Log File ------------")
    fobj.write(Border+"\n")

    fobj.close()

def main():

    Border = "-"*60
    print(Border)
    print("----------Marvellous platform Surveilence System----------")
    print(Border)

    #--h and --u handing
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to perform")
            print("1:It fetch the information of running processes")
            print("2:It fetch the information about the primary storage as RAM")
            print("3:It fetch the information about the secondary primary storage as HDD")
            print("4:It fetch the information about the microprocessor")
            print("5:Gets auto scheduled periodically")
            print("6:It maintains all records log file")
            print("7:It sends log fils through mail periodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as : ")
            print(f"python {sys.argv[0]} Time_interval Folder_Name ")
            print("Time_Interval :Time in minutes for periodic Excution")
            print("Folder Name : Name of folder for the log file creation")
        else:
            print("unable to proceed as arguments are not matching")
            print("please use --h or --u flag for getting more details")

    #actual project code
    elif(len(sys.argv)== 3):
        #print("CPU USAGE : ",psutil.cpu_percent()) #to calculate percentage of cpu usage 
        print("Schedular Started Sucessfully")
        print("press Ctrl + c to abort Automation Script")

        #schedular
        schedule.every(int(sys.argv[1])).minutes.do(PlatformSurveilence,sys.argv[2])

        while(True):
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid Number of arguments")
        print("unable to proceed as arguments are not matching")
        print("please use --h or --u flag for getting more details")

    
    print(Border)
    print("Thank you for using our automation system")
    print(Border)

if __name__ == "__main__":
    main()