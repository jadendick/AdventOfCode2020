file = open("input","r")

def part1():

    length = 31 # Length of each line
    position = 0
    count = 0

    for line in file:
        if(position == 0): # Skip first line
            position += 3
            continue
            
        if(line[position%length] == "#"):
            count += 1
        
        position += 3

    print(count)

def part2():
    length = 31 # Length of each line
    lineNum = 0

    moveRight = [1,3,5,7,1] # Distance to move right for each slope
    positions = [0,0,0,0,0] # Current position for each slope
    counts = [0,0,0,0,0] # Current tree count for each slope

    for line in file:
        if(lineNum == 0): # Skip first line
            lineNum += 1            
            for i in range(5):
                positions[i] += moveRight[i]
            continue

        if(lineNum%2 != 0):
            positions[4] -= 1            

        for i in range(5):
            if(line[positions[i]%length]=="#" and (i!=4 or lineNum%2==0)):
                counts[i] += 1
            positions[i] += moveRight[i]
        
        lineNum += 1            

    print(counts[0]*counts[1]*counts[2]*counts[3]*counts[4])

# part1()
part2()
file.close()