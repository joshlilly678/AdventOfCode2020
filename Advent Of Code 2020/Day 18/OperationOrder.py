
def read_input(fname):
    with open(fname, "r") as file:
        return [x.strip() for x in file.readlines()]

def parseInput(inputFile):
    out = []
    for line in inputFile:
        # Get Characters
        chars = []
        chars[:] = line
        for char in chars:
            if char == " ":
                chars.remove(char)
        out.append(chars)
    return out

def evalExpressionPart1(chars):
    # base case
    if type(chars) is int:
        return int(chars)

    # Split line on top level operation
    nodes = [''] 
    ops = []
    i = 0
    while i < len(chars):
        if chars[i].isnumeric():
            nodes[-1] += chars[i]
        elif chars[i] in ["+", "*"]:
            ops.append(chars[i])
            nodes.append('')
        elif chars[i] == "(":
            i += 1
            depth = 1 # keep track of depth of brackets 
            while depth > 0:
                if chars[i] == "(":
                    depth += 1
                elif chars[i] == ")":
                    depth -= 1
                nodes[-1] += chars[i]
                i += 1
            nodes[-1] = nodes[-1][:-1] # remove closing bracket for this 'node'
            i -= 1
        i += 1
        
    while len(nodes) >= 2:
        if ops[0] == "+":
            nodes[1] = evalExpressionPart1(nodes[0]) + evalExpressionPart1(nodes[1])
        elif ops[0] == "*":
            nodes[1] = evalExpressionPart1(nodes[0]) * evalExpressionPart1(nodes[1])
        del nodes[0]
        del ops[0]
        
    return int(nodes[0])
    
def evalExpressionPart2(chars):
    # base case
    if type(chars) is int:
        return int(chars)

    # Split line on top level operation
    nodes = [''] 
    ops = []
    i = 0
    while i < len(chars):
        if chars[i].isnumeric():
            nodes[-1] += chars[i]
        elif chars[i] in ["+", "*"]:
            ops.append(chars[i])
            nodes.append('')
        elif chars[i] == "(":
            i += 1
            depth = 1 # keep track of depth of brackets 
            while depth > 0:
                if chars[i] == "(":
                    depth += 1
                elif chars[i] == ")":
                    depth -= 1
                nodes[-1] += chars[i]
                i += 1
            nodes[-1] = nodes[-1][:-1] # remove closing bracket for this 'node'
            i -= 1
        i += 1
        
    while len(nodes) >= 2:
        if "+" in ops:
            ind = ops.index("+")
            nodes[ind+1] = evalExpressionPart2(nodes[ind]) + evalExpressionPart2(nodes[ind+1])
            del nodes[ind]
            del ops[ind]
        else:
            nodes[1] = evalExpressionPart2(nodes[0]) * evalExpressionPart2(nodes[1])
            del nodes[0]
            del ops[0]
        
    return int(nodes[0])
    
def part1(lines):
    out = []
    for line in lines:
        out.append(evalExpressionPart1(line))
    return sum(out)
    
def part2(lines):
    out = []
    for line in lines:
        out.append(evalExpressionPart2(line))
    return sum(out)
      
def main():
    inputFile = read_input("input.txt")
    lines = parseInput(inputFile)
    print("The answer to part 1 is " + str(part1(lines)))
    print("The answer to part 2 is " + str(part2(lines)))    

if __name__ == "__main__":
    main()