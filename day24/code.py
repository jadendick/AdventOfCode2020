import re
file = open("input","r")
input = file.read().splitlines()
dirs = []
for i in input:
    n = re.sub("se"," se ",i)
    n = re.sub("sw"," sw ",n)
    n = re.sub("nw"," nw ",n)
    n = re.sub("ne"," ne ",n)
    n = re.sub("ee"," e e ",n)
    n = re.sub("ww"," w w ",n)
    n = re.sub("we"," w e ",n)
    n = re.sub("ew"," e w ",n)
    n = re.sub("  "," ",n)
    dirs.append(n)

blackTiles = {}

def part1():
    black = {}

    for dir in dirs:
        n,e = 0,0

        dir = dir.split(" ")
        for d in dir:
            if(d == "ne"):
                e += .5
                n += 1
            elif(d == "nw"):
                e -= .5
                n += 1
            elif(d == "se"):
                e += .5
                n -= 1
            elif(d == "sw"):
                e -= .5
                n -= 1
            elif(d == "e"):
                e += 1
            elif(d == "w"):
                e -= 1

        c = (n,e)
        if(c in black):
            black.pop(c)
        else:
            black.update({ c : True })

    global blackTiles
    blackTiles = dict(black)
    return len(black)

def part2():
    global blackTiles

    d = [(0,1),(0,-1),(1,.5),(1,-.5),(-1,.5),(-1,-.5)]
    for turn in range(100):
        newBlack = {}
        checkWhite = {}
        for b in blackTiles:
            blackCount = 0
            for dx in d:
                bx = (b[0]+dx[0], b[1]+dx[1])
                if(blackTiles.get(bx)):
                    blackCount += 1
                checkWhite.update({ bx : True })

            if(blackCount == 1 or blackCount == 2):
                newBlack.update({ b : True})

        for b in checkWhite:
            blackCount = 0
            for dx in d:
                bx = (b[0]+dx[0], b[1]+dx[1])
                if(blackTiles.get(bx)):
                    blackCount += 1
                    
            if(blackCount == 2):
                newBlack.update({ b : True})

        blackTiles = dict(newBlack)

    return len(blackTiles)

print("Part 1: ",part1())
print("Part 2: ",part2())

file.close()