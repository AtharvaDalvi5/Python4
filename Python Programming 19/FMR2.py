CheckEven = lambda No: (No % 2 == 0)
Square = lambda No: No * No
Addition = lambda No1, No2: No1 + No2

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
    Ans = 0

    for no in Elements:
        Ans = Task(Ans, no)

    return Ans

def main():
    Data = [5,2,3,4,3,4,1,2,8,10]

    print("Input Data :", Data)

    FData = list(filterX(CheckEven, Data))
    print("Data after Filter :", FData)

    MData = list(mapX(Square, FData))
    print("Data after Map :", MData)

    RData = reduceX(Addition, MData)
    print("Data after Reduce :", RData)

if __name__ == "__main__":
    main()