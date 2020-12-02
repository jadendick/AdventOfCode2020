file = open("input","r")
valid = 0

for line in file:
    split = line.split(" ")
    positions = split[0].split("-")
    letter = split[1][0]
    password = split[2]
    count = 0

    c1 = password[int(positions[0])-1]
    c2 = password[int(positions[1])-1]

    if(bool(c1 == letter) ^ bool(c2 == letter)):
        valid += 1

print(valid)
file.close()