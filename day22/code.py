file = open("input","r")
input = file.read().split("\n\n")
deck1 = [int(x) for x in input[0].split("\n")[1:]]
deck2 = [int(x) for x in input[1].split("\n")[1:-1]]


def part1():
    s = 0

    while(len(deck1) != 0 and len(deck2) != 0):
        c1 = deck1.pop(0)
        c2 = deck2.pop(0)
        if(c1 > c2):
            deck1.append(c1)
            deck1.append(c2)
        else:
            deck2.append(c2)
            deck2.append(c1)

    win = deck1 if len(deck1)!=0 else deck2
    for i,x in enumerate(win[::-1]):
        s += x*(i+1)

    return s

def part2():
    s = 0


    return s

print("Part 1: ",part1())
print("Part 2: ",part2())

file.close()