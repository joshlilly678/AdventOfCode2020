# read in file
def read_input(fname):
    with open(fname) as file:
        return [x.strip() for x in file.readlines()]  

def part1and2(inputs):
    #init highest seat id to 0 - for part 1
    out = 0

    maxSeatId = 127*8 + 7
    SeatIds = list(range(0,maxSeatId+1))

    for x in inputs:
        totalRows = list(range(0, 128))
        totalCols = list(range(0, 8))

        # find row
        Row = totalRows
        n = len(totalRows)
        for i in x:
            if i in ["F", "B"]:
                n /= 2
                if i == "F":
                    Row = Row[:int(n)]
                if i == "B":
                    Row = Row[int(n):2*int(n)]
            else:
                continue
            
        Row = Row[0]

        # find col
        Col = totalCols
        n = len(totalCols)
        for i in x:
            if i in ["R", "L"]:
                n /= 2
                if i == "L":
                    Col = Col[:int(n)]
                if i == "R":
                    Col = Col[int(n):2*int(n)]
            else:
                continue
            
        Col = Col[0]
        
        seatId = Row * 8 + Col
        SeatIds.remove(seatId)
     
        # For part 1
        if seatId > out:
            out = seatId

    ans = []
    for i in SeatIds:
        if i + 1 in SeatIds or i - 1 in SeatIds:
            continue
        else:
            ans.append(i)

    # The answers
    print("The answer to part 1 is " + str(out))
    print("The answer to part 2 is " + str(ans[0]))

def main():
    inputFile = read_input("input.txt")
    part1and2(inputFile)
    
if __name__ == "__main__":
    main()






