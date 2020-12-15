file = open("input","r")
input = [int(x) for x in file.read().split("\n")[:-1][0].split(",")]

def part1():
    turn = 0
    spoken = {}
    for i,x in enumerate(input):
        spoken.update({ x: i })
        turn += 1
        
    lastSpoken = input[-1]
    while(turn < 2020):
        ls = spoken.get(lastSpoken)
        spoken.update({ lastSpoken : turn-1 })
        lastSpoken = 0 if ls==None or ls==turn-1 else turn-ls-1
        turn += 1
    
    return lastSpoken

def part2():
    turn = 0
    spoken = {}
    for i,x in enumerate(input):
        spoken.update({ x: i })
        turn += 1
        
    lastSpoken = input[-1]
    while(turn < 30000000):
        ls = spoken.get(lastSpoken)
        spoken.update({ lastSpoken : turn-1 })
        lastSpoken = 0 if ls==None or ls==turn-1 else turn-ls-1
        turn += 1
    
    return lastSpoken

print("Part 1: ",part1())
print("Part 2: ",part2())

file.close()