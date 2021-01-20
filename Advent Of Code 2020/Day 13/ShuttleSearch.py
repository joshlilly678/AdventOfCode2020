import bisect

def read_input(fname):
    with open(fname, "r") as file:
        return [x.strip() for x in file.readlines()]

def getRunningBusIds(inputFile):
    estimate = inputFile[0]
    busIds = inputFile[1].split(",")
    return int(estimate), busIds
    
def remove(busIds, val):
    runningBusIds = []
    for v in busIds:
        if v != val:
            runningBusIds.append(int(v))
    return runningBusIds
    
def getNextBusTimes(estimate, busIds):
    busTimeTable = {}
    for bus in busIds:
        if bus not in busTimeTable:
            busTimeTable[bus] = []
        else:
            continue
        for i in range(estimate+1000):
            if i % bus == 0:
                busTimeTable[bus].append(i)
        pos = bisect.bisect_left(busTimeTable[bus], estimate)
        busTimeTable[bus] = busTimeTable[bus][pos:pos+1]
    return busTimeTable

def part1(estimate, busTimeTable):
    minVal = min(busTimeTable.values())
    minValKey = []
    for key in busTimeTable:
        if busTimeTable[key] == minVal:
            minValKey.append(key)
    return minValKey[0] * (minVal[0]-estimate)
    
def part2(inputFile, busIds):
    BusWithPos = []
    for pos, bus in enumerate(busIds):
        if bus != "x":
            BusWithPos.append([pos,int(bus)])
    timestamp = 0
    p = 1
    for deltaTime, bus in BusWithPos:
        while True:
            if (deltaTime + timestamp) % bus == 0:
                break
            timestamp += p
        p *= bus
    return timestamp
    
def main():
    inputFile = read_input("input.txt")
    estimate, busIds = getRunningBusIds(inputFile)
    runningBusIds = remove(busIds, "x")
    busTimeTable = getNextBusTimes(estimate, runningBusIds)
    
    print("The answer to part 1 is " + str(part1(estimate, busTimeTable)))
    print("The answer to part 2 is " + str(part2(inputFile, busIds)))
   
if __name__ == "__main__":
    main()
    