file = open("input","r")
input = file.read().split("\n")[:-1]

def part1():
    prevRan = {}
    lineNum = 0
    acc = 0

    while(not prevRan.get(lineNum)):
        prevRan.update({ lineNum : True })
        line = input[lineNum]
        if(line[:3] == "acc"):
            acc += int(line[4:])
            lineNum += 1
        elif(line[:3] == "jmp"):
            lineNum += int(line[4:])
        else:
            lineNum += 1

    return acc

def part2():
    totalLines = len(input)
    prevRan = {}
    lineNum = 0
    acc = 0
    changedLine = -1 # Hold a jmp/nop line that is changed and the acc/prevRan at that time


    while(lineNum < totalLines):

        if(prevRan.get(lineNum)):
            lineNum = changedLine[0]
            acc = changedLine[1]
            prevRan = changedLine[2]
            changedLine = -1

            line = input[lineNum]

            if(line[:3] == "jmp"):
                lineNum += int(line[4:])
            else:
                lineNum += 1

        else:
            oldLineNum = lineNum
            line = input[lineNum]
            prevRan.update({ oldLineNum : True })
        
            if(line[:3] == "acc"):
                acc += int(line[4:])
                lineNum += 1
            elif(line[:3] == "jmp"):
                if(changedLine == -1): # Treat like nop
                    changedLine = (lineNum,acc,dict(prevRan))
                    lineNum += 1
                else:
                    lineNum += int(line[4:])
            else:
                if(changedLine == -1): # Treat like jmp
                    changedLine = (lineNum,acc,dict(prevRan))
                    lineNum += int(line[4:])
                else:
                    lineNum += 1
            


    return acc

print("Part 1: ",part1())
print("Part 2: ",part2())

file.close()