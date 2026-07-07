import threading

def Small(Str):
    Count = 0

    print(f"Thread ID :",{ threading.get_ident()})
    print(f"Thread Name :", {threading.current_thread().name})

    for c in Str:
        if c.islower():
            Count = Count + 1

    print("Small letters :", Count)
    print()

def Capital(Str):
    Count = 0

    print(f"Thread ID :",{ threading.get_ident()})
    print(f"Thread Name :", {threading.current_thread().name})

    for c in Str:
        if c.isupper():
            Count = Count + 1

    print("Capital letters :", Count)
    print()

def Digit(Str):
    Count = 0

    print(f"Thread ID :",{ threading.get_ident()})
    print(f"Thread Name :", {threading.current_thread().name})

    for c in Str:
        if c.isdigit():
            Count = Count + 1

    print("Digit :", Count)
    print()

def main():
    Str = input("Enter a string : ")

    T1 = threading.Thread(target=Small, args=(Str,), name="Small")
    T2 = threading.Thread(target=Capital, args=(Str,), name="Capital")
    T3 = threading.Thread(target=Digit, args=(Str,), name="Digit")

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

if __name__ == "__main__":
    main()
