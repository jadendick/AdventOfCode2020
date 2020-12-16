import re
file = open("input","r")
input = file.read().split("\n\n")

nearby = input[2][16:].split("\n")[:-1]
nearbyDiscard = list(nearby)
rules = dict()
for x in [x.split(": ") for x in input[0].split("\n")]:
    r = x[1].split(" or ")
    rules.update({ x[0] : [[int(a) for a in r[0].split("-")],[int(a) for a in r[1].split("-")]] })

def passes(x):
    p = set()
    for rule in rules:
        ruleVal = rules.get(rule)
        if((x >= ruleVal[0][0] and x <= ruleVal[0][1]) or (x >= ruleVal[1][0] and x <= ruleVal[1][1])):
            p.add(rule)
    return p

def part1():
    sum = 0

    for y in nearby:
        valid = False
        for x in y.split(","):
            x = int(x)
            valid = False
            for rule in rules.values():
                if((x >= rule[0][0] and x <= rule[0][1]) or (x >= rule[1][0] and x <= rule[1][1])):
                    valid = True
                    break            
            if(not valid):
                sum += int(x)
                nearbyDiscard.remove(y)
                break

    return sum

def part2():
    sum = 1
    myTicket = input[1][13:]
    ticketLen = len(myTicket.split(","))
    passed = [set() for x in range(ticketLen)]
    
    nearbyDiscard.insert(0,myTicket)

    for ticket in nearbyDiscard:
        for i,num in enumerate(ticket.split(",")):
            p = passes(int(num))
            if(len(passed[i]) == 0):
                passed[i] = p
            else:
                passed[i] = set.intersection(p,passed[i])


    decoded = {}
    while(len(decoded.keys()) < ticketLen):
        for i,x in enumerate(passed):
            if(len(x) == 1):
                val = list(x)[0]
                decoded.update({ i : val })
                for a in passed:
                    if(val in a):
                        a.remove(val)

    myTicket = myTicket.split(",")
    for i in range(len(decoded.values())):
        if("departure" in decoded.get(i)):
            sum *= int(myTicket[i])
        
    return sum

print("Part 1: ",part1())
print("Part 2: ",part2())

file.close()