file = open("input","r")
input = file.read().split("\n")[:-1]
active = {}
newMap = {}

def getCount3(coord):
    x,y,z = coord
    count = 0

    for dz in range(-1,2):
        for dy in range(-1,2):
            for dx in range(-1,2):  
                if((dx,dy,dz) != (0,0,0)):
                    if(active.get((x+dx,y+dy,z+dz))):
                        count += 1
                    if(count == 4):
                        return count

    return count

def getCount4(coord):
    x,y,z,w = coord
    count = 0

    for dw in range(-1,2):
        for dz in range(-1,2):
            for dy in range(-1,2):
                for dx in range(-1,2):  
                    if((dx,dy,dz,dw) != (0,0,0,0)):
                        if(active.get((x+dx,y+dy,z+dz,w+dw))):
                            count += 1
                        if(count == 4):
                            return count

    return count

def part1():
    global active
    global newMap

    for y,r in enumerate(input):
        for x,c in enumerate(r):
            if(c == "#"):
                active.update({ (x,y,0) : True })
    
    newMap = dict(active)

    for cycle in range(6):
        for z in range(-10,10):
            for y in range(-30,30):
                for x in range(-30,30):
                    coord = (x,y,z)
                    count = getCount3(coord)
                    cur = newMap.get(coord)
                    if(cur):
                        if(count != 2 and count != 3):
                            newMap.pop(coord)
                    elif(count == 3):
                        newMap.update({ coord : True })
        active = dict(newMap)

    return len(active)

def part2():
    global active
    global newMap

    active = {}
    newMap = {}

    for y,r in enumerate(input):
        for x,c in enumerate(r):
            if(c == "#"):
                active.update({ (x,y,0,0) : True })
    
    newMap = dict(active)

    for cycle in range(6):
        for w in range(-10,10):
            for z in range(-10,10):
                for y in range(-30,30):
                    for x in range(-30,30):
                        coord = (x,y,z,w)
                        count = getCount4(coord)
                        cur = newMap.get(coord)
                        if(cur):
                            if(count != 2 and count != 3):
                                newMap.pop(coord)
                        elif(count == 3):
                            newMap.update({ coord : True })
        active = dict(newMap)

    return len(active)

print("Part 1: ",part1())
print("Part 2: ",part2())

file.close()