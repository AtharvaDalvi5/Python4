import threading
import time

def EvenFactor(No):
    Sum = 0
    print("Even Factors:")
    for i in range(1, No + 1):
        if No % i == 0 and i % 2 == 0:
            print(i, end=" ")
            Sum = Sum + i
    print("Sum of Even Factors =", Sum)

def OddFactor(No):
    Sum = 0
    print("Odd Factors:")
    for i in range(1, No + 1):
        if No % i == 0 and i % 2 != 0:
            print(i, end=" ")
            Sum = Sum + i
    print("Sum of Odd Factors =", Sum)

def main():
    print("Enter the Number : ")
    No = int(input())

    strat_time = time.perf_counter()

    T1 = threading.Thread(target=EvenFactor, args=(No,))
    T2 = threading.Thread(target=OddFactor, args=(No,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    end_time = time.perf_counter()

    print(f"time required is : {end_time-strat_time:.4f}")

    print("Exit from main....")

if __name__ == "__main__":
    main()