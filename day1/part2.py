file = open("input","r")

values = []

for line in file:    
    current = int(line)
    values.append(current)

    for old1 in values:
        for old2 in values:
            if(old1 + old2 + current == 2020):
                print(old1 * old2 * current)

file.close()