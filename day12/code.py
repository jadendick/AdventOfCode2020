file = open("input","r")
input = file.read().split("\n")[:-1]

def part1():
    north = 0
    east = 0
    facing = 1
    for x in input:
        dir = x[0]
        mag = int(x[1:])

        if(dir == "N"):
            north += mag
        elif(dir == "S"):
            north -= mag
        elif(dir == "E"):
            east += mag
        elif(dir == "W"):
            east -= mag
        elif(dir == "F"):
            if(facing == 0):
                north += mag
            elif(facing == 1):
                east += mag
            elif(facing == 2):
                north -= mag
            elif(facing == 3):
                east -= mag
        elif(dir == "R"):
            facing = (facing + mag/90) % 4
        elif(dir == "L"):
            facing = (facing - mag/90) % 4
            
    return abs(east) + abs(north)


def part2():
    north = 0
    east = 0
    wnorth = 1
    weast = 10
    for x in input:
        dir = x[0]
        mag = int(x[1:])

        if(dir == "N"):
            wnorth += mag
        elif(dir == "S"):
            wnorth -= mag
        elif(dir == "E"):
            weast += mag
        elif(dir == "W"):
            weast -= mag
        elif(dir == "F"):
            north += wnorth * mag
            east += weast * mag
        elif(dir == "R"):
            deg = mag/90 % 4
            if(deg == 1):
                onorth = wnorth
                wnorth = -weast
                weast = onorth
            elif(deg == 2):
                wnorth = -wnorth
                weast = -weast
            elif(deg == 3):
                onorth = wnorth
                wnorth = weast
                weast = -onorth
            
        elif(dir == "L"):
            deg = mag/90 % 4
            if(deg == 1):
                onorth = wnorth
                wnorth = weast
                weast = -onorth
            elif(deg == 2):
                wnorth = -wnorth
                weast = -weast
            elif(deg == 3):
                onorth = wnorth
                wnorth = -weast
                weast = onorth
            
    return abs(east) + abs(north)

print("Part 1: ",part1())
print("Part 2: ",part2())

file.close()