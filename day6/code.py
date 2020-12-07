input = open("input","r").read().split("\n\n")

def part1():
    sum = 0
    for i in input:
        questions = set()
        for line in i.split("\n"):
            questions.update(line)
        sum += len(questions)

    return(sum)

def part2():
    sum = 0
    for i in input:
        lines = i.split("\n")
        common = set(lines[0])

        for line in lines[1:]:
            if(line != ""):
                common = common.intersection(set(line))
        
        sum += len(common)
        
    return(sum)

print("Part 1: ",part1())
print("Part 2: ",part2())