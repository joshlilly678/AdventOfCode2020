
def read_input(fname):
    with open(fname, "r") as file:
        return [list(x.strip()) for x in file.readlines()]
        
def getInitialActiveCoords(inputFile):
    activeCoords = []
    for y in range(len(inputFile)):
        row = inputFile[y]
        for x in range(len(row)):
            coord = row[x]
            if coord == '#':
                activeCoords.append([x,y,0,0])
    return activeCoords
    
def getInitialBounds(inputFile):
    # bounds = [x_start, x_size, y_start, y_size, z_start, z_size, w_start, w_size]
    bounds = [0, len(inputFile[0]), 0, len(inputFile), 0, 1, 0, 1]
    return bounds
    
def findNeighboursCoords(point):
    x = point[0]
    y = point[1]
    z = point[2]
    w = point[3]
    neighbours = []
    for a in [-1, 0, 1]:
        for b in [-1, 0, 1]:
            for c in [-1, 0, 1]:
                for d in [-1, 0, 1]:
                    if a==b==c==d==0:
                        continue
                    neighbours.append([x+a,y+b,z+c,w+d])
    return neighbours
    
def applyRules(activeCoords, bounds):
    # increase bounds for next cycle
    bounds = bounds.copy()
    for i in range(len(bounds)):
        if i % 2 == 0: # if x, y or z start pos: then decrease by 1
            bounds[i] = bounds[i] - 1
        else: # if x, y, z size:then increase by 2
            bounds[i] = bounds[i] + 2
    
    newActiveCoords = []
    for x in range(bounds[0],bounds[1]):
        for y in range(bounds[2], bounds[3]):
            for z in range(bounds[4], bounds[5]):
                for w in range(bounds[6], bounds[7]):
                    coord = [x, y, z, w]
                    count = 0
                    for c in findNeighboursCoords(coord):
                        if c in activeCoords:
                            count += 1
                        if count > 3:
                            break 
                    if coord in activeCoords:
                        if count in [2, 3]:
                            newActiveCoords.append(coord)
                    else:
                        if count == 3:
                            newActiveCoords.append(coord)
    return newActiveCoords, bounds
    
def part2(activeCoords, bounds):
    for _ in range(6):
        activeCoords, bounds = applyRules(activeCoords, bounds)
    return len(activeCoords)
    
def main():
    inputFile = read_input("input.txt")
    activeCoords = getInitialActiveCoords(inputFile)
    bounds = getInitialBounds(inputFile)
    print(part2(activeCoords, bounds))

if __name__ == "__main__":
    main()