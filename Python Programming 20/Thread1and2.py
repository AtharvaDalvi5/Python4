import threading

def Display1():
    print("Thread1:")
    for i in range(1, 51):
        print(i, end=" ")
    print()

def Display2():
    print("Thread2:")
    for i in range(50, 0, -1):
        print(i, end=" ")
    print()

def main():
    T1 = threading.Thread(target=Display1, name="Thread1")
    T2 = threading.Thread(target=Display2, name="Thread2")

    T1.start()
    T1.join()      
    
    T2.start()
    T2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()