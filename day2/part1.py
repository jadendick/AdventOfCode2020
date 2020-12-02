file = open("input","r")
valid = 0

for line in file:
    split = line.split(" ")
    minmax = split[0].split("-")
    letter = split[1][0]
    count = 0

    for x in split[2]:
        if(x == letter):
            count += 1

    if count in range(int(minmax[0]),int(minmax[1])+1):
        valid += 1           

print(valid)
file.close()