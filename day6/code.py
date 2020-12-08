from functools import reduce
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
        lines = i.rstrip().split("\n")
        common = list(reduce(lambda a,b : a.intersection(b), [ set(x) for x in lines ]))
        sum += len(common)
        
    return sum

print("Part 1: ",part1())
print("Part 2: ",part2())