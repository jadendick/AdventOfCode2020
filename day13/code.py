file = open("input","r")
input = file.read().split("\n")[:-1]
time = int(input[0])
routes = []
split = input[1].split(",")
for x in range(len(split)):
    if(split[x] != "x"):
        routes.append((int(split[x]),x)) 

def part1():
    min = -1
    id = 0

    for x in routes:
        x = x[0]
        diff = int(time / x) * x - time
        if(diff < 0):
            diff = x+diff
        if(diff < min or min == -1):
            id = x
            min = diff
    
    return min*id

def part2():
    found = False
    departTime = 0
    jump = routes[0][0]

    while(not found):
        departTime = departTime + jump
        jump = 1
        found = True
        for x in routes:
            if((departTime + x[1]) % x[0] != 0):
                found = False
                break
            else:
                jump *= x[0] # Set jump to lcm of busses that are already lined up
                
    return departTime


print("Part 1: ",part1())
print("Part 2: ",part2())

file.close()