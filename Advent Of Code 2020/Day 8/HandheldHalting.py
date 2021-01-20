def read_input(fname):
    with open(fname, "r") as file:
        return [x.strip() for x in file.readlines()]

def getInstructions(inputFile):
    count = 0
    instructions = {}
    for i in inputFile:
        i = i.split(" ")
        i[1] = int(i[1])
        i.append("n")
        instructions[count] = i
        count += 1
    return instructions

def followInstruction(instructions, start, acc):
    if start >= len(instructions)-1:
        return acc
    ins = instructions[start] # get dictionary value
    if ins[2] == 'y': # if used, return acc
        return acc
    # apply rules
    if ins[0] == 'nop': 
        val = start + 1
    if ins[0] == 'acc':
        acc += ins[1]
        val = start + 1
    if ins[0] == 'jmp':
        val = start + ins[1]
    # specify this key is now used
    ins[2] = 'y'
    # recursively call 
    return followInstruction(instructions, val, acc)
    
def FindEnd(instructions, start, acc):
    if start == len(instructions)-1:
        return "end"
    ins = instructions[start] # get dictionary value
    if ins[2] == 'y': 
        return start
    if ins[0] == 'nop':
        val = start + 1
    if ins[0] == 'acc':
        acc += ins[1]
        val = start + 1
    if ins[0] == 'jmp':
        val = start + ins[1]
    ins[2] = 'y'
    return FindEnd(instructions, val, acc)
    
def Part2(instructions):
    for x, y in instructions.items():
        temp = {}
        # swap nop and jmp if either
        if y[0] == 'nop':
            y[0] = 'jmp'
        elif y[0] == 'jmp':
            y[0] = 'nop'

        eip = FindEnd(instructions, 0, 0)
        
        if eip == 'end':
            temp = instructions
            for x, y in temp.items():
                y[2] = 'n'
            return followInstruction(temp, 0, 0)
        
        # revert back as the swap did not correct the code
        if y[0] == 'nop':
            y[0] = 'jmp'
        elif y[0] == 'jmp':
            y[0] = 'nop'
        
        for x, y in instructions.items():
            y[2] = 'n'
        
def main():
    inputFile = read_input("input.txt")
    instructions = getInstructions(inputFile)
    print("The answer to part 1 is " + str(followInstruction(instructions, 0, 0)))
    print("The answer to part 2 is " + str(Part2(instructions)))
    

if __name__ == "__main__":
    main()