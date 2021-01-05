file = open("input","r")
input = file.read().splitlines()
key1 = int(input[0])
key2 = int(input[1])
subject = 7

print("Key 1",key1)
print("Key 2",key2)

def getLoopSize(key):
    v = 1
    loopSize = 0

    while v != key:
        v *= 7
        v %= 20201227
        loopSize += 1

    return loopSize

def transform(subject, loopSize):
    v = 1
    for loop in range(loopSize):
        v *= subject
        v %= 20201227

    return v


print("Part 1: ",transform(key2,getLoopSize(key1)))

file.close()