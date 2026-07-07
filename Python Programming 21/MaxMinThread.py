import threading

def Max(Data):
    print("Maximum element =", max(Data))

def Min(Data):
    print("Minimum element =", min(Data))

def main():
    Size = int(input("Enter number of elements: "))

    Data = []

    print("Enter elements:")
    for i in range(Size):
        No = int(input())
        Data.append(No)

    T1 = threading.Thread(target=Max, args=(Data,))
    T2 = threading.Thread(target=Min, args=(Data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()