file = open("input","r")
input = [int(x) for x in file.read().split("\n")[:-1]]

def part1():
    sum = 0

    for x in range(25,len(input)):
        values = input[x-25:x]
        valid = False

        for a in range(len(values)):
            for b in range(len(values[a:])):
                if(values[a]+values[a+b] == input[x]):
                    valid = True
        if(not valid):
            sum = input[x]
            break
                    
    
    return sum

def part2():
    invalidNum = part1()
    arr = []

    for a in range(len(input)):
        contigSum = input[a]
        for b in range(1,len(input[a:])):
            contigSum += input[a+b]
            if(contigSum == invalidNum):
                arr = input[a:a+b]
                break

    return min(arr) + max(arr)

print("Part 1: ",part1())
print("Part 2: ",part2())

file.close()