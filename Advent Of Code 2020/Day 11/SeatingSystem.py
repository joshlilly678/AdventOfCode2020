import copy

def read_input(fname):
    with open(fname, "r") as file:
        return [list(x.strip()) for x in file.readlines()]

def neighbours(arr, radius, rowNumber, columnNumber):
    t = []
    for i in range(rowNumber-1-radius, rowNumber+radius):
        for j in range(columnNumber-1-radius, columnNumber+radius):
            if  i >= 0 and i < len(arr) and j >= 0 and j < len(arr[0]):
                t.append(arr[i][j])
            else:
                t.append(0)
    return t
    
def directions():
    topLeft = [-1,-1]
    top = [-1,0]
    topRight = [-1,1]
    midLeft = [0,-1]
    midRight = [0,1]
    botLeft = [1,-1]
    bot = [1,0]
    botRight = [1,1]
    return [topLeft, top, topRight, midLeft, midRight, botLeft, bot, botRight]
    
def neighboursPart2(arr, row, col):
    t = []
    dirs = directions()
    for d in dirs:
        tRow = copy.deepcopy(row)
        tCol = copy.deepcopy(col)
        x = "."
        while x == ".":
            tRow += d[0]
            tCol += d[1]
            if tRow >= 0 and tRow < len(arr) and tCol >= 0 and tCol < len(arr[0]):
                x = arr[tRow][tCol]
            else:
                x = 0
        t.append(x)
    return t
    
def applyPart1Rules(arr):
    temp = copy.deepcopy(arr)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            n = neighbours(arr, 1, i+1, j+1)
            if arr[i][j] == '.':
                continue
            elif arr[i][j] == "L":
                for x in n:
                    if x == '#':
                        break
                else:
                    temp[i][j] = "#"
            elif arr[i][j] == '#':
                count = 0
                for x in n:
                    if x == '#':
                        count += 1
                if count > 4:
                    temp[i][j] = 'L'
    return temp

def applyPart2Rules(arr):
    temp = copy.deepcopy(arr)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            n = neighboursPart2(arr,i,j)
            if arr[i][j] == '.':
                continue
            elif arr[i][j] == "L":
                for x in n:
                    if x == '#':
                        break
                else:
                    temp[i][j] = "#"
            elif arr[i][j] == '#':
                count = 0
                for x in n:
                    if x == '#':
                        count += 1
                if count > 4:
                    temp[i][j] = 'L'
    return temp
    
def runPart1(arr):
    temp = applyPart1Rules(arr)
    if temp == arr:
        count = 0
        for x in temp:
            for y in x:
                if y == "#":
                    count += 1
        return count
    else:
        return runPart1(temp)
        
def runPart2(arr):
    temp = applyPart2Rules(arr)
    if temp == arr:
        count = 0
        for x in temp:
            for y in x:
                if y == "#":
                    count += 1
        return count
    else:
        return runPart2(temp)
        
def main():
    inputFile = read_input("input.txt")
    print("The answer to part 1 is " + str(runPart1(inputFile)))
    print("The answer to part 2 is " + str(runPart2(inputFile)))

if __name__ == "__main__":
    main()