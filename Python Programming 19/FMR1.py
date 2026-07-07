Check = lambda No: (No >= 70 and No <= 90)
Increase = lambda No: No + 10
Product = lambda No1, No2: No1 * No2

def filterX(Task, Elements):
    Result = []

    for no in Elements:
        if(Task(no)):
            Result.append(no)

    return Result

def mapX(Task, Elements):
    Result = []

    for no in Elements:
        Result.append(Task(no))

    return Result

def reduceX(Task, Elements):
    Ans = 1

    for no in Elements:
        Ans = Task(Ans, no)

    return Ans

def main():
    Data = [4,34,36,76,68,24,89,23,86,90,45,70]

    print("Input Data :", Data)

    FData = list(filterX(Check, Data))
    print("Data after Filter :", FData)

    MData = list(mapX(Increase, FData))
    print("Data after Map :", MData)

    RData = reduceX(Product, MData)
    print("Data after Reduce :", RData)

if __name__ == "__main__":
    main()