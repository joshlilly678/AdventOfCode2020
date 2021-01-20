# read in file
def read_input(fname):
    with open(fname) as file:
        return [x.strip() for x in file.readlines()]   

### PART 1 ###
def part1(inputs):
    # init count of valid passwords
    validCount = 0

    # for each password
    for i in inputs:
        arr = i.split(" ")
        arr[0] = arr[0].split("-")
        arr[1] = arr[1][0]
        
        low_num = int(arr[0][0])
        high_num = int(arr[0][1])
        letter = arr[1]
        password = arr[2]
        
        count = password.count(letter)
        
        if count >= low_num and count <= high_num:
            validCount += 1
        
    print("The answer to part 1 is " + str(validCount))

### Part 2 ###
def part2(inputs):
    # init count of valid passwords
    validCount = 0

    # for each password
    for i in inputs:
        arr = i.split(" ")
        arr[0] = arr[0].split("-")
        arr[1] = arr[1][0]
        
        low_num = int(arr[0][0])
        high_num = int(arr[0][1])
        letter = arr[1]
        password = arr[2]
        
        if password[low_num-1] == letter and password[high_num-1] != letter:
            validCount += 1
        elif password[low_num-1] != letter and password[high_num-1] == letter:
            validCount += 1
        
    print("The answer to part 2 is " + str(validCount))
    
def main():
    inputFile = read_input("input.txt")
    part1(inputFile)
    part2(inputFile)
    
if __name__ == "__main__":
    main()