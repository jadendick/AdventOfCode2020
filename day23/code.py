cupsInput = [int(x) for x in "523764819"]
cups = list(cupsInput)
cl = len(cups)

def pickUp(x):
    pos = cups.index(x)

    up = [ cups[(pos+1)%cl], cups[(pos+2)%cl], cups[(pos+3)%cl] ]

    for c in up:
        cups.remove(c)

    return up

def part1():

    global cups
    curIndex = 0
    curVal = cups[curIndex]

    for turn in range(100):
        destVal = curVal - 1
        if(destVal < 1):
            destVal = 9
            
        up = pickUp(curVal)
        
        while destVal in up:
            destVal -= 1
            if(destVal < 1):
                destVal = 9

        destIndex = cups.index(destVal)
        cups = cups[:destIndex+1] + up + cups[destIndex+1:]
        
        curIndex = (cups.index(curVal)+1) % cl
        curVal = cups[curIndex]

    ind = cups.index(1)
    return "".join(map(str,cups[ind+1:] + cups[:ind]))

def part2():
    cupMap = {}
    cups = list(cupsInput)

    for x in range(10,1000001):
        cups.append(x)

    cl = len(cups)
    for i,c in enumerate(cups):
        cupMap.update({ c : cups[(i+1)%cl] })
    
    curVal = cupsInput[0]

    for turn in range(10000000):
        destVal = curVal - 1
        if(destVal < 1):
            destVal = 1000000
            
        up = []
        next = cupMap.get(curVal)
        up.append(next)
        next = cupMap.get(next)
        up.append(next)
        next = cupMap.get(next)
        up.append(next)

        cupMap.update({ curVal : cupMap.get(up[2]) })
        
        while destVal in up:
            destVal -= 1
            if(destVal < 1):
                destVal = 1000000

        temp = cupMap.get(destVal)
        cupMap.update({ destVal : up[0] })
        cupMap.update({ up[2] : temp })
        
        curVal = cupMap.get(curVal)

    return cupMap.get(1) * cupMap.get(cupMap.get(1))

print("Part 1: ",part1())
print("Part 2: ",part2())
