# read in file
def read_input(fname):
    with open(fname, "r") as file:
        return [int(x.strip()) for x in file.readlines()]

def findFirstError(inputFile):
    length = len(inputFile)
    for num in inputFile:
        ind = inputFile.index(num)
        if ind > length - 26:
            break
        for i in inputFile[ind:ind + 25]:
            compliment = inputFile[ind+25] - i
            if compliment in inputFile[ind:ind + 25] and compliment != i:
                break
        else:
            return inputFile[ind+25] # The Answer
            break

def findNumSet(inputFile, invalidNum):
    length = len(inputFile)
    numSet = []
    for i in range(0, len(inputFile)):
        for j in range(1, len(inputFile)):
            temp = inputFile[i:j]
            if sum(temp) == invalidNum:
                return min(temp) + max(temp) # The Answer
                
def findNumSetImproved(inputFile, invalidNum):
    highPointer = 2
    lowPointer = 0
    x = inputFile[lowPointer:highPointer]
    for i in range(0, len(inputFile)):
        if sum(x) == invalidNum:
            return max(x) + min(x)
        elif sum(x) > invalidNum:
            lowPointer += 1
            x = inputFile[lowPointer:highPointer]
            #print(x)
        elif sum(x) < invalidNum:
            highPointer += 1
            x = inputFile[lowPointer:highPointer]
            #print(x)
           
def main():
    inputFile = read_input("input.txt")
    invalidNum = findFirstError(inputFile) 
    print("The answer to part 1: " + str(invalidNum))
    print("The answer to part 2: " + str(findNumSetImproved(inputFile, invalidNum)))

if __name__ == "__main__":
    main()