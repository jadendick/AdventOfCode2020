file = open("input","r")

values = []

for line in file:    
    current = int(line)
    values.append(current)

    for old in values:
        if(old + current == 2020):
            print(old * current)

file.close()