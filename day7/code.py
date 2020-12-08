import re

file = open("input","r")
input = file.read().split("\n")[:-1]

adjList = {}
containsGold = {}

def hasGold(bag):
    if(containsGold.get(bag)):
        return True

    insideBags = adjList.get(bag)

    for insideBag in insideBags if insideBags!=None else []:
        if(insideBag == "shiny gold" or hasGold(insideBag)):
            containsGold.update({bag: True})
            return True

def contains(bag):
    num = 0
    bagVal = re.split(" ",bag,1)
    insideBags = adjList.get(bagVal[1])

    for insideBag in insideBags:
        if(insideBag == "no other"):
            num = 0
        else:
            num += contains(insideBag)

    return int(bagVal[0]) + int(bagVal[0]) * num

def part1():
    global adjList
    adjList = {}
    for line in input:
        parts = re.split(" bags*(?: contain \d |\, \d |\.)",line)
        adjList.update({ parts[0] : parts[1:-1] })
        
    sum = 0
    for bag in adjList.keys():
        if(hasGold(bag)):
            sum += 1

    return sum

def part2():
    global adjList
    adjList = {}
    for line in input:
        parts = re.split(" bags*(?: contain |\, |\.)",line)
        adjList.update({parts[0]:parts[1:-1]})

    sum = 0
    for bag in adjList.get("shiny gold"):
        sum += contains(bag)
    
    return sum

print("Part 1: ",part1())
print("Part 2: ",part2())

file.close()