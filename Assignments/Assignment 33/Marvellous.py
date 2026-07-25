import os
import hashlib

def CalculateChkSum(FileName):

    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()


def FindDuplicate(DirectoryName):

    Ret = os.path.exists(DirectoryName)

    if(Ret == False):
        return {}

    Ret = os.path.isdir(DirectoryName)

    if(Ret == False):
        return {}

    Duplicate = {}

    TotalFiles = 0

    for FolderName,SubFolder,FileName in os.walk(DirectoryName):

        for fname in FileName:

            TotalFiles = TotalFiles + 1

            fname = os.path.join(FolderName,fname)

            CheckSum = CalculateChkSum(fname)

            if CheckSum in Duplicate:
                Duplicate[CheckSum].append(fname)
            else:
                Duplicate[CheckSum] = [fname]

    return Duplicate,TotalFiles


def DeleteDuplicate(DirectoryName,LogFile):

    Data,TotalFiles = FindDuplicate(DirectoryName)

    Result = list(filter(lambda x : len(x) > 1 , Data.values()))

    TotalDeleted = 0
    DuplicateFound = 0

    fobj = open(LogFile,"a")

    fobj.write("---------------------------------------------------\n")

    for value in Result:

        DuplicateFound = DuplicateFound + (len(value)-1)

        count = 0

        for subvalue in value:

            count = count + 1

            if(count > 1):

                try:

                    os.remove(subvalue)

                    fobj.write("Deleted File : "+subvalue+"\n")

                    TotalDeleted = TotalDeleted + 1

                except Exception as E:

                    fobj.write("Unable to delete : "+subvalue+"\n")

                    fobj.write(str(E)+"\n")

        count = 0

    fobj.write("\n")

    fobj.write("Total Files Scanned : "+str(TotalFiles)+"\n")

    fobj.write("Duplicate Files Found : "+str(DuplicateFound)+"\n")

    fobj.write("Duplicate Files Deleted : "+str(TotalDeleted)+"\n")

    fobj.write("---------------------------------------------------\n")

    fobj.close()

    return TotalDeleted