file = open("input","r")

def part1():
    maxCode = 0
    for line in file:
        rowMin = 0
        rowMax = 128
        for x in line[:7]:
            if(x=="F"):
                rowMax -= (rowMax-rowMin) / 2
            else:
                rowMin += (rowMax-rowMin) / 2

        colMin = 0
        colMax = 8
        for x in line[7:-1]:
            if(x=="L"):
                colMax -= (colMax-colMin) / 2
            else:
                colMin += (colMax-colMin) / 2

        maxCode = max(maxCode, rowMin*8+colMin) 

    print(maxCode)

def part2():
    seats = [False] * 1024
    for line in file:
        rowMin = 0
        rowMax = 128
        for x in line[:7]:
            if(x=="F"):
                rowMax -= (rowMax-rowMin) / 2
            else:
                rowMin += (rowMax-rowMin) / 2

        colMin = 0
        colMax = 8
        for x in line[7:-1]:
            if(x=="L"):
                colMax -= (colMax-colMin) / 2
            else:
                colMin += (colMax-colMin) / 2

        seats[int(rowMin*8+colMin)] = True 

    for x in range(1,1023):
        if(not seats[x] and seats[x-1] and seats[x+1]):
            print(x)

# part1()
part2()

file.close()