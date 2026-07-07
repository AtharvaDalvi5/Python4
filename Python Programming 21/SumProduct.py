import threading

def Addition(Data, Sum):
    Sum[0] = 0

    for i in Data:
        Sum[0] = Sum[0] + i

def Multiplication(Data, Product):
    Product[0] = 1

    for i in Data:
        Product[0] = Product[0] * i

def main():
    print("Enter the Number: ")
    No = int(input())

    Data = []

    print("Enter elements:")
    for i in range(No):
        No = int(input())
        Data.append(No)

    Sum = [0]
    Product = [1]

    T1 = threading.Thread(target=Addition, args=(Data, Sum))
    T2 = threading.Thread(target=Multiplication, args=(Data, Product))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Sum =", Sum[0])
    print("Product =", Product[0])

if __name__ == "__main__":
    main()