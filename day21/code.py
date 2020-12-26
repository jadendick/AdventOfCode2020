file = open("input","r")
input = [x[:-1].split(" (contains ") for x in file.read().splitlines()]
file.close()

allergenIngs = {}
for food in input:
    for allergen in food[1].split(", "):
        inew = set(food[0].split(" "))
        iold = allergenIngs.get(allergen) if allergenIngs.get(allergen)!=None else inew
        allergenIngs.update({ allergen : iold.intersection(inew) })


def part1():
    aIngs = set()
    for a in [x for y in allergenIngs for x in allergenIngs.get(y)]:
        aIngs.add(a)
        
    return len([word for line in input for word in line[0].split(" ") if not word in aIngs])

def part2():
    decoded = {}
    while(len(decoded) < len(allergenIngs)):
        for i in allergenIngs:
            a = allergenIngs.get(i).difference(decoded.values())
            allergenIngs.update({ i : a })
            if(len(a) == 1):
                decoded.update({ i : a.pop() })
                break

    alpha = list(decoded.keys())
    alpha.sort()
    return ",".join(decoded.get(a) for a in alpha)[:-1]

print("Part 1: ",part1())
print("Part 2: ",part2())
