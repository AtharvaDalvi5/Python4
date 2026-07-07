import threading
import time

def Even():
    print("First 10 Even Numbers:")
    for i in range(2, 21, 2):
        print(i, end=" ")
    print()

def Odd():
    print("First 10 Odd Numbers:")
    for i in range(1, 20, 2):
        print(i, end=" ")
    print()

def main():
    strat_time = time.perf_counter()
    T1 = threading.Thread(target=Even)
    T2 = threading.Thread(target=Odd)

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    end_time = time.perf_counter()

    print(f"time required is : {end_time-strat_time:.4f}")

if __name__ == "__main__":
    main()