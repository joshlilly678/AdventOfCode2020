# read in file
def read_input(fname):
    with open(fname) as file:
        inputs = file.read()
        return inputs.split('\n\n')

def part1(inputs):
    count = 0
    for group in inputs:
        group = group.replace("\n", "") # ensure input is on the same line to read
        group = list(group)
        uniqueYes = set(group)
        count += len(uniqueYes)
    print(count)

def part2(inputs):
    count = 0
    for group in inputs:
        raw = group
        group = group.replace("\n", " ") # ensure input is on the same line to read
        group = group.split(" ")
        numGroup = len(group)
        
        raw = raw.replace("\n", "") # ensure input is on the same line to read
        counter = 0
        for i in range(97, 123):  #loop through alphabet 
            x = raw.count(chr(i))
            if x == numGroup: # check if letter is in full group string for all people in group 
                # i.e check if whole group answer yes for question
                counter += 1
        count += counter
    print(count)
    
def main():
    inputFile = read_input("input.txt")
    part1(inputFile)
    part2(inputFile)
    
if __name__ == "__main__":
    main()