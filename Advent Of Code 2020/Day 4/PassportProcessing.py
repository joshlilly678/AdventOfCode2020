import re

# read in file
def read_input(fname):
    with open(fname) as file:
        inputs = file.read()
        return inputs.split('\n\n')

def part1(inputs):
    count = 0 # init count
    for i in inputs:
        i = i.replace("\n", " ") # ensure input is on the same line to read
        if "byr:" in i and "iyr:" in i and "eyr:" in i and "hgt:" in i and "hcl:" in i and "ecl:" in i and "pid:" in i:
            count += 1
    print(count)

def part2(inputs):
    count = 0
    for i in inputs:
        i = i.replace("\n", " ") # ensure input is on the same line to read
        i = i.split(" ")
        if len(i) > 8:
            i.pop(8)
        #print(i)
        dic = dict(j.split(":", 1) for j in i)
        #print(dic)
        
        regex = "^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"
        p = re.compile(regex)
        
        if "byr" in dic.keys() and "iyr" in dic.keys() and "eyr" in dic.keys() and "hgt" in dic.keys() and "hcl" in dic.keys() and "ecl" in dic.keys() and "pid" in dic.keys():
            if len(dic["byr"]) != 4 or int(dic["byr"]) < 1920 or int(dic["byr"]) > 2002:
                continue
            if len(dic["iyr"]) != 4 or int(dic["iyr"]) < 2010 or int(dic["iyr"]) > 2020:
                continue
            if len(dic["eyr"]) != 4 or int(dic["eyr"]) < 2020 or int(dic["eyr"]) > 2030:
                continue
            if "cm" not in dic["hgt"] and "in" not in dic["hgt"]:
                continue
            if "cm" in dic["hgt"]:
                x = len(dic["hgt"]) - 2
                if int(dic["hgt"][:x]) < 150 or int(dic["hgt"][:x]) > 193:
                    continue
            if "in" in dic["hgt"]:
                x = len(dic["hgt"]) - 2
                if int(dic["hgt"][:x]) < 59 or int(dic["hgt"][:x]) > 76:
                    continue
            if dic["hcl"][0] != "#":
                continue
            if len(dic["hcl"]) != 7:
                continue
            if not re.search(p, dic["hcl"]):
                continue
            if dic["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                continue
            if len(dic["pid"]) != 9:
                continue
            count += 1
    print(count)
    
def main():
    inputFile = read_input("input.txt")
    part1(inputFile)
    part2(inputFile)
    
if __name__ == "__main__":
    main()
    
    
    
    