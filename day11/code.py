file = open("input","r")
input = [list(x) for x in file.read().split("\n")[:-1]]
inputLen = len(input)
lineLen = len(input[0])

def part1():
    sum = 0
    newInput = [list(x) for x in input]
    inp = [list(x) for x in input]

    while(True):
        for x in range(inputLen):
            for y in range(lineLen):
                occ = 0
                shift = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
                for i in shift:
                    xs = x+i[0]
                    ys = y+i[1]
                    if(xs>=0 and ys>=0 and xs<inputLen and ys<lineLen and inp[xs][ys]=="#"):
                        occ += 1

                if(inp[x][y] != "." and occ == 0):
                    newInput[x][y] = "#"
                if(inp[x][y] == "#" and occ >= 4):
                    newInput[x][y] = "L"

        if(newInput == inp):
            break
                    
        inp = [list(x) for x in newInput]

    for x in newInput:
        sum += x.count("#")

    return sum


def part2():
    sum = 0
    newInput = [list(x) for x in input]
    inp = [list(x) for x in input]

    while(True):
        for x in range(inputLen):
            for y in range(lineLen):
                occ = 0

                shift = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
                for i in shift:
                    z = 1
                    xs = x+i[0]
                    ys = y+i[1]
                    while(xs>=0 and ys>=0 and xs<len(inp) and ys<lineLen and inp[xs][ys]=="."):
                        z += 1
                        xs = x+i[0]*z
                        ys = y+i[1]*z

                    if(xs>=0 and ys>=0 and xs<inputLen and ys<lineLen and inp[xs][ys]=="#"):
                        occ += 1

                if(inp[x][y] != "." and occ == 0):
                    newInput[x][y] = "#"
                if(inp[x][y] == "#" and occ >= 5):
                    newInput[x][y] = "L"

        if(newInput == inp):
            break
        inp = [list(x) for x in newInput]

    for x in newInput:
        sum += x.count("#")

    return sum

print("Part 1: ",part1())
print("Part 2: ",part2())

file.close()