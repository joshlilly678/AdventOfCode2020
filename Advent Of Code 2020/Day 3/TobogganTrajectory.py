# read in file
def read_input(fname):
    with open(fname) as file:
        return [x.strip() for x in file.readlines()]  

def part1(inputs, right):
    # find len of each line (this is constant)
    lineLen = len(inputs[0])
    
    x = 0 # Init index each path
    count = 0 # Init Count each path
    for pos in inputs:
        if pos[x] == '#':
            count += 1
        x += right
        x = x % lineLen
    print("The answer to part 1 is " + str(count))

def part2(inputs):
    # find len of each line (this is constant)
    lineLen = len(inputs[0])

    # Number of steps to the "right"
    rightList = [1, 3, 5, 7]

    #Init outList
    outList = []

    for right in rightList:
        x = 0 # Init index each path
        count = 0 # Init Count each path
        for pos in inputs:
            if pos[x] == '#':
                count += 1
            x += right
            x = x % lineLen
        
        outList.append(count)
        
    x = 0 # init index for final path
    count = 0 # init count for final path
    for pos in inputs:
        index = inputs.index(pos)
        if index % 2 == 0:
            if pos[x] == '#':
                count += 1
            x += 1
            x = x % lineLen
    outList.append(count)

    # print(outList)
    ans = outList[0]*outList[1]*outList[2]*outList[3]*outList[4]
    print("The answer to part 2 is " + str(ans))
    
def main():
    inputFile = read_input("input.txt")
    part1(inputFile, 3)
    part2(inputFile)
    
if __name__ == "__main__":
    main()

