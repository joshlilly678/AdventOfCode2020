# read in file
def read_input(fname):
    with open(fname, "r") as file:
        return [int(x.strip()) for x in file.readlines()]

def findDeviceVoltage(inputFile):
    return max(inputFile)+3
    
def findDifferenceAndMultiply(inputFile, deviceVoltage):
    sort = sorted(inputFile)
    oneJoltDif = 0
    twoJoltDif = 0 
    threeJoltDif = 1 #initialises at 1 for your device to last input
    for i in range(0,len(sort)):
        if i == 0:
            if sort[i] > 3:
                break
            if sort[i] == 1:
                oneJoltDif += 1
            if sort[i] == 2:
                twoJoltDif += 1
            if sort[i] == 3:
                threeJoltDif += 1
        else:
            if sort[i] - sort[i-1] > 3:
                break
            if sort[i] - sort[i-1] == 1:
                oneJoltDif += 1
            if sort[i] - sort[i-1] == 2:
                twoJoltDif += 1
            if sort[i] - sort[i-1] == 3:
                threeJoltDif += 1
    return oneJoltDif * threeJoltDif
    
def findDiffs(inputFile, deviceVoltage):
    sort = sorted(inputFile)
    diffs = []
    for i in range(0,len(sort)):
        if i == 0:
            if sort[i] > 3:
                break
            if sort[i] == 1:
                diffs.append(1)
            if sort[i] == 2:
                diffs.append(2)
            if sort[i] == 3:
                diffs.append(3)
        else:
            if sort[i] - sort[i-1] > 3:
                break
            if sort[i] - sort[i-1] == 1:
                diffs.append(1)
            if sort[i] - sort[i-1] == 2:
                diffs.append(2)
            if sort[i] - sort[i-1] == 3:
                diffs.append(3)
    diffs.append(3)
    return diffs # extra 3 on end for your device
    
def findPaths(inputFile):
    inputFile.sort()
    inputFile.reverse()
    path = {x:0 for x in inputFile} # create dictionary with all values at -1
    path.update({0:0}) # add 0th item, the charge port
    path[inputFile[0]] = 1 # update last value (first in reversed) to 1
    for key in path: # loop through the dictionary keys
        if key != inputFile[0]: 
            sum = 0
            for x in range(1,4): # for each time key+(1,2or3) is in dictionary add to path 
                if key+x in path:
                    sum = sum + path[key+x]
            path[key] = sum
    return path[0]

def main():
    inputFile = read_input("input.txt")
    deviceVoltage = findDeviceVoltage(inputFile)
    print("The answer for part 1 is "+ str(findDifferenceAndMultiply(inputFile, deviceVoltage)))
    print("The answer for part 2 is "+ str(findPaths(inputFile)))
   
if __name__ == "__main__":
    main()
   