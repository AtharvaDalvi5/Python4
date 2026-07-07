import threading

def Increment(Counter, Lock):
    for i in range(1000):
        Lock.acquire()
        Counter[0] = Counter[0] + 1
        Lock.release()

def main():
    Counter = [0]
    Lock = threading.Lock()

    T1 = threading.Thread(target=Increment, args=(Counter, Lock))
    T2 = threading.Thread(target=Increment, args=(Counter, Lock))
    T3 = threading.Thread(target=Increment, args=(Counter, Lock))

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

    print("Final Counter =", Counter[0])

if __name__ == "__main__":
    main()