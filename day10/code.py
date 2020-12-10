file = open("input","r")
input = sorted([int(x) for x in file.read().split("\n")[:-1]])
input.insert(0,0)
adj = {}

def part1():
    sum1 = 0
    sum3 = 0
    jolt = 0

    for x in input:
        if(x - jolt == 1):
            sum1 += 1    
        elif(x - jolt == 3):
            sum3 += 1    
        jolt = x

    return sum1 * (sum3+1)

splits = {}
def countBranch(b):
    if(splits.get(b) != None):
        return splits.get(b)

    count = 0
    for x in adj.get(b) if adj.get(b)!=None else []:
        if(x == input[-1]):
            count += 1
        count += countBranch(x)

    splits.update({ b : count })
    return count

def part2():

    for x in range(len(input)):
        cur = input[x]
        if(x+3 < len(input) and input[x+3] <= cur+3):
            adj.update({ cur : input[x+1:x+4] })
        elif(x+2 < len(input) and input[x+2] <= cur+3):
            adj.update({ cur : input[x+1:x+3] })
        elif(x+1 < len(input)):
            adj.update({ cur : [input[x+1]] })
    
    return countBranch(input[0])
    


print("Part 1: ",part1())
print("Part 2: ",part2())

file.close()