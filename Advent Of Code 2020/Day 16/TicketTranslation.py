
def readInput(inputFile):
    with open(inputFile) as file:
        inputs = file.read()
        inputs = inputs.split('\n\n')
        
        # get fields
        inputs[0] = inputs[0].split("\n")
        fields = {}
        for i in inputs[0]:
            i = i.split(": ")
            rng = i[1].split(" or ")
            for j in range(len(rng)):
                rng[j] = rng[j].split("-")
                
            fields[i[0]] = rng
        
        # get your ticket
        inputs[1] = inputs[1].split(":\n")
        yourTicket = inputs[1][1]
        
        # get nearby tickets
        inputs[2] = inputs[2].split(":\n")
        n = inputs[2][1].split("\n")
        nearbyTickets = []
        for ticket in n:
            nearbyTickets.append(ticket.split(","))
        
        return fields, yourTicket, nearbyTickets
        
def transformRules(fields):
    for key in fields:
        temp = [list(map(int, x)) if isinstance(x, list) else int(x) for x in fields[key]]
        fields[key] = [tuple(l) for l in temp]
    return fields

def findInvalidTicketErrorRate(fields, nearbyTickets):
    count = 0
    for ticket in nearbyTickets:
        for val in ticket:
            for key in fields:
                if (int(val) >= int(fields[key][0][0]) and int(val) <= int(fields[key][0][1])) or (int(val) >= int(fields[key][1][0]) and int(val) <= int(fields[key][1][1])):
                    break
            else:
                count += int(val)
    return count
    
def findInvalidTickets(fields, nearbyTickets):
    invalidTickets = []
    for ticket in nearbyTickets:
        for val in ticket:
            for key in fields:
                if (int(val) >= int(fields[key][0][0]) and int(val) <= int(fields[key][0][1])) or (int(val) >= int(fields[key][1][0]) and int(val) <= int(fields[key][1][1])):
                    break
            else:
                invalidTickets.append(ticket)
    return invalidTickets
    
def removeInvalidTickets(nearbyTickets, invalidTickets):
    validTickets = []
    for ticket in nearbyTickets:
        if ticket not in invalidTickets:
            for i in range(len(ticket)):
                ticket[i] = int(ticket[i])
            validTickets.append(ticket)
    return validTickets
    
def findTicketOrder(fields, validTickets):
    # dict mapping each index in a ticket to the fields that are possible for that index
    possibleFields = {i: set(fields.keys()) for i in range(len(validTickets[0]))}
    for ticket in validTickets:
        for i, value in enumerate(ticket):
            for key in fields:
                possible = False
                for lo, hi in fields[key]:
                    if lo <= value <= hi:
                        possible = True
                        break
                if not possible:
                    possibleFields[i].discard(key)
    # print(possibleFields)

    # Some indices fit multiple fields – iterate through the ones that only fit one first, and
    # remove this field from all other indices
    for i in sorted(possibleFields, key=lambda k: len(possibleFields[k])):
        thisField = next(iter(possibleFields[i]))
        for j in possibleFields:
            if i != j:
                possibleFields[j].discard(thisField)
    
    return possibleFields # ordered list of key fields
    
def findAnswer(orderedList, yourTicket):
    yourTicket = yourTicket.split(",")
    ans = 1
    for i in orderedList:
        if orderedList[i].pop().startswith("departure"):
            ans *= int(yourTicket[i])
    return ans

def main():
    fields, yourTicket, nearbyTickets = readInput("input.txt")
    print("The answer to part 1 is " + str(findInvalidTicketErrorRate(fields, nearbyTickets)))
    invalidTickets = findInvalidTickets(fields, nearbyTickets)
    validTickets = removeInvalidTickets(nearbyTickets, invalidTickets)
    fields = transformRules(fields)
    orderedList = findTicketOrder(fields, validTickets)
    print("The answer to part 2 is " + str(findAnswer(orderedList, yourTicket)))
    
    
if __name__ == "__main__":
    main()