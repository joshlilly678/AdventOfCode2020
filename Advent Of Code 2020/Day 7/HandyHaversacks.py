def getBagRules(file):
    rules = open(file, 'r')
    bags = {}
    for bagRule in rules:
        rule = {}
        bagRule = bagRule.replace('.', '')
        bag, rules = bagRule.split(' contain ')
        bag = bag.replace('bags', 'bag')
        rules = rules.split(',')
        
        for r in rules:
            if 'other' in r:
                continue
            else:
                r = r.strip()
                r = r.replace('bags', 'bag')
                rule[r[2:]] = r[:1]
        bags[bag] = rule
    return bags
    

def containers(inner, rules):
    outer = []
    for rule in rules:
        for r in rules[rule]:
            if inner in r:
                outer.append(rule)
    for bag in outer:
        temp = containers(bag, rules)
        for t in temp:
            if t not in outer:
                outer.append(t)
    return outer
    

def inside(outer, rules):
    total = 0
    # if bag contains another bag(s)
    if len(rules[outer]) != 0:  
        for bag in rules[outer]:
            temp = inside(bag, rules)
            total = total + (temp*int(rules[outer][bag]))
    total += 1 # add 1 for bag itself
    return total
    

def main():
    rules = getBagRules("input.txt")
    print("The answer to part 1 is " + str(len(containers("shiny gold", rules))))
    print("The answer to part 2 is " + str(inside('shiny gold bag', rules)-1))
        
if __name__ == "__main__":
    main()