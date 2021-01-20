import itertools
import copy

def read_input(fname):
    with open(fname, "r") as file:
        return [x.strip().split(" = ") for x in file.readlines()]

def part1(inputFile):
    values = {}
    for line in inputFile:
        if line[0] == "mask":
            mask = list(line[1])
        else:
            # get memory, i.e key of dictionary
            l = len(line[0])
            memPos = line[0][4:l-1] 
            
            # get value in bin format and make it to len 36 to check against mask
            valList = list(bin(int(line[1])))
            del valList[0:2] # delete the preamble "0b"
            while len(valList) < 36:
                valList.insert(0,'0')
            
            # override where applicable 
            for i in range(len(mask)):
                if mask[i] == "X":
                    continue
                else:
                    valList[i] = mask[i]
                    
            # add to values dictionary
            v = "".join(valList)
            v = int(v,2)
            values[memPos] = v
    return sum(values.values())
    
def getAllCombos(memList):
    combos = list(itertools.product("10", repeat=memList.count("X")))
    floatingBits = []
    for combo in combos:
        memCopy = copy.deepcopy(memList)
        c = 0
        for i in range(len(memList)):
            if memList[i] == 'X':
                memCopy[i] = combo[c]
                c += 1
        floatingBits.append(memCopy)
    return floatingBits
    
def part2(inputFile):
    values = {}
    for line in inputFile:
        if line[0] == "mask":
            mask = list(line[1])
        else:
            # get memory, i.e key of dictionary
            l = len(line[0])
            memPos = line[0][4:l-1] 
            
            # get memory and make it to len 36 to check against mask
            memList = list(bin(int(memPos)))
            del memList[0:2] # delete the preamble "0b"
            while len(memList) < 36:
                memList.insert(0,'0')
            
            # override where applicable 
            for i in range(len(mask)):
                if mask[i] == "0":
                    continue
                elif mask[i] == "1":
                    memList[i] = mask[i]
                elif mask[i] == "X":
                    memList[i] = mask[i]
            
            # add to values dictionary
            floatingBits = getAllCombos(memList)
            for memPos in floatingBits:
                m = "".join(memPos)
                m = int(m,2)
                values[m] = int(line[1])
                
    return sum(values.values())

def main():
    inputFile = read_input("input.txt")
    print("The answer to part 1 is: " + str(part1(inputFile)))
    print("The answer to part 2 is: " + str(part2(inputFile)))
    
if __name__ == "__main__":
    main()