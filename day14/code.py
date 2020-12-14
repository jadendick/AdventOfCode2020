file = open("input","r")
input = file.read().split("\n")[:-1]

def part1():
    mask = []
    memory = {}

    for x in input:
        if(x[:4] == "mask"):
            mask = [(i,x) for i,x in enumerate(x[7:]) if x != "X"]
        else:
            addr = x[4:x.index("]")]
            binVal = bin(int(x[x.index("=")+2:]))[2:].zfill(36)

            for i in mask: # Insert mask values into binary value
                binVal = binVal[:i[0]] + i[1] + binVal[i[0]+1:]

            memory.update({ addr : int(binVal,2) })

    return sum(memory.values())

def part2():
    maskX = []
    mask1 = []
    memory = {}

    for x in input:
        if(x[:4] == "mask"):
            mask = x[7:]
            maskX = [i for i,x in enumerate(mask) if x == "X"]
            mask1 = [i for i,x in enumerate(mask) if x == "1"]

        else:
            binAddr = bin(int(x[4:x.index("]")]))[2:].zfill(36)
            val = int(x[x.index("=")+2:])

            for i in mask1:
                binAddr = binAddr[:i]+"1"+binAddr[i+1:]
            for i in maskX:
                binAddr = binAddr[:i]+"0"+binAddr[i+1:]

            offsets = [2**(35-i) for i in maskX]
            allOffsets = []

            def subsetSums(left, right, sum=0): 
                if left > right: 
                    allOffsets.append(sum) 
                    return
                subsetSums(left+1, right, sum + offsets[left]) # Subset including arr[left] 
                subsetSums(left+1, right, sum) # Subset excluding arr[left] 

            subsetSums(0,len(offsets)-1)

            baseAddr = int(binAddr,2)
            for a in allOffsets:
                memory.update({ baseAddr+a : val })

    return sum(memory.values())

print("Part 1: ",part1())
print("Part 2: ",part2())

file.close()