import threading

def Small(Str):
    Cnt = 0

    for ch in Str:
        if(ch.islower()):
            Cnt = Cnt + 1

    print("Thread Name :", threading.current_thread().name)
    print("Thread ID :", threading.get_ident())
    print("Small letters :", Cnt)

def Capital(Str):
    Cnt = 0

    for ch in Str:
        if(ch.isupper()):
            Cnt = Cnt + 1

    print("Thread Name :", threading.current_thread().name)
    print("Thread ID :", threading.get_ident())
    print("Capital letters :", Cnt)

def Digits(Str):
    Cnt = 0

    for ch in Str:
        if(ch.isdigit()):
            Cnt = Cnt + 1

    print("Thread Name :", threading.current_thread().name)
    print("Thread ID :", threading.get_ident())
    print("Digits :", Cnt)

def main():
    Value = input("Enter string : ")

    T1 = threading.Thread(target=Small, args=(Value,), name="Small")
    T2 = threading.Thread(target=Capital, args=(Value,), name="Capital")
    T3 = threading.Thread(target=Digits, args=(Value,), name="Digits")

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

    print("Exit from main")

if __name__ == "__main__":
    main()