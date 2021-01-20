    
def part1(StartingNumbers, number):
    # initialise current state of the game
    gameDic = {}
    count = 1
    for num in StartingNumbers:
        gameDic[count] = num
        count += 1
    
    for turn in range(1, number+1):
        vals = list(gameDic.values())
        if turn in gameDic.keys():
            continue
        else:
            prev = gameDic[turn-1]
            val = vals.count(prev)
            if val == 1:
                gameDic[turn] = 0
            elif val > 1:
                indices = [i+1 for i, x in enumerate(vals) if x == prev]
                gameDic[turn] = (indices[-1]-indices[-2])
    return gameDic[number]
    
def part2(StartingNumbers, number):
    # initialise currentState of the game
    currentState = {
        "lastInd": dict(zip(StartingNumbers[:-1], range(len(StartingNumbers)-1))),
        "lastNum": StartingNumbers[-1],
        "len": len(StartingNumbers)
    }
    # print(currentState)

    for turn in range(len(StartingNumbers), number):
        lastNum = currentState["lastNum"]
        if lastNum in currentState["lastInd"]:
            prevInd = currentState["lastInd"][lastNum]
            newNum = currentState["len"] - prevInd - 1
        else:
            newNum = 0
        
        # Update current state of game
        currentState["lastInd"][lastNum] = currentState["len"] - 1 # If doesnt exist: override, otherwise add new key
        currentState["len"] += 1 # Iterated for calculations
        currentState["lastNum"] = newNum
    return currentState["lastNum"]

def main():
    # StartingNumbers = [0,3,6]
    StartingNumbers = [0,1,5,10,3,12,19]
    print("The answer to part 1 is " + str(part1(StartingNumbers, 2020)))
    print("The answer to part 2 is " + str(part2(StartingNumbers, 30000000)))
    
if __name__ == "__main__":
    main()
