file = open("input","r")
input = file.read().split("\n\n")
deck1 = [int(x) for x in input[0].split("\n")[1:]]
deck2 = [int(x) for x in input[1].split("\n")[1:-1]]


def part1():
    s = 0

    d1 = list(deck1)
    d2 = list(deck2)

    while(len(d1) != 0 and len(d2) != 0):
        c1 = d1.pop(0)
        c2 = d2.pop(0)
        if(c1 > c2):
            d1.append(c1)
            d1.append(c2)
        else:
            d2.append(c2)
            d2.append(c1)

    win = d1 if len(d1)!=0 else d2
    for i,x in enumerate(win[::-1]):
        s += x*(i+1)

    return s

def subGame(d1,d2): # Return true if p1 wins
    prev = []
    while(len(d1) != 0 and len(d2) != 0):
        if((d1,d2) in prev):
            return True
        prev.append((list(d1),list(d2)))

        c1 = d1.pop(0)
        c2 = d2.pop(0)

        if(len(d1) >= c1 and len(d2) >= c2):
            if subGame(list(d1[:c1]),list(d2[:c2])):
                d1.append(c1)
                d1.append(c2)
            else:
                d2.append(c2)
                d2.append(c1)

        elif(c1 > c2):
            d1.append(c1)
            d1.append(c2)
        else:
            d2.append(c2)
            d2.append(c1)

    return len(d1)!=0

def part2():
    s = 0

    d1 = list(deck1)
    d2 = list(deck2)

    prev = []
    while(len(d1) != 0 and len(d2) != 0):
        if((d1,d2) in prev):
            return True
        prev.append((list(d1),list(d2)))

        c1 = d1.pop(0)
        c2 = d2.pop(0)
        
        if(len(d1) >= c1 and len(d2) >= c2):
            if subGame(list(d1[:c1]),list(d2[:c2])):
                d1.append(c1)
                d1.append(c2)
            else:
                d2.append(c2)
                d2.append(c1)

        elif(c1 > c2):
            d1.append(c1)
            d1.append(c2)
        else:
            d2.append(c2)
            d2.append(c1)

    win = d1 if len(d1)!=0 else d2
    for i,x in enumerate(win[::-1]):
        s += x*(i+1)

    return s

print("Part 1: ",part1())
print("Part 2: ",part2())

file.close()