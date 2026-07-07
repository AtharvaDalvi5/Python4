def CheckPrime(No):
    if No < 2:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True

Multiply = lambda No: No * 2
Maximum = lambda No1, No2: No1 if(No1 > No2) else No2

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
    Ans = Elements[0]

    for no in Elements[1:]:
        Ans = Task(Ans, no)

    return Ans

def main():
    Data = [2,70,11,10,17,23,31,77]

    print("Input Data :", Data)

    FData = list(filterX(CheckPrime, Data))
    print("Data after Filter :", FData)

    MData = list(mapX(Multiply, FData))
    print("Data after Map :", MData)

    RData = reduceX(Maximum, MData)
    print("Data after Reduce :", RData)

if __name__ == "__main__":
    main()