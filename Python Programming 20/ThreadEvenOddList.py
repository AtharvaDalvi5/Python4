import threading
import time

def EvenList(Data):
    Sum = 0
    print("Even Elements:")
    for i in Data:
        if i % 2 == 0:
            print(i, end=" ")
            Sum = Sum + i
    print("\nSum of Even Elements =", Sum)

def OddList(Data):
    Sum = 0
    print("Odd Elements:")
    for i in Data:
        if i % 2 != 0:
            print(i, end=" ")
            Sum = Sum + i
    print("\nSum of Odd Elements =", Sum)

def main():
    print("Enter the Number : ")
    No = int(input())

    Data = []

    print("Enter elements:")
    for i in range(No):
        No = int(input())
        Data.append(No)

    strat_time = time.perf_counter()

    T1 = threading.Thread(target=EvenList, args=(Data,))
    T2 = threading.Thread(target=OddList, args=(Data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    end_time = time.perf_counter()

    print(f"time required is : {end_time-strat_time:.4f}")

if __name__ == "__main__":
    main()