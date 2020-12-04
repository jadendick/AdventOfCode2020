from os import truncate
import re
file = open("input","r")

def part1():
    count = 0
    values = []
    for line in file:
        if(line != "\n"):
            values += line.split(" ")
        else:
            if(len(values) == 8 or (len(values) == 7 and (len(list(filter (lambda x : x.split(":")[0] == "cid", values))) == 0))):
                count += 1
            values = []
    print(count)

def part2():
    count = 0
    values = []
    for line in file:
        if(line != "\n"):
            values += line.split(" ")
        else:
            if(len(values) == 8 or (len(values) == 7 and (len(list(filter (lambda x : x.split(":")[0] == "cid", values))) == 0))):
                fields = {}
                for value in values:
                    valueSplit = value.split(":")
                    fields[valueSplit[0]] = valueSplit[1]

                byr = int(fields.get("byr"))
                iyr = int(fields.get("iyr"))
                eyr = int(fields.get("eyr"))
                hgtValid = False

                if(re.search(".*cm",fields.get("hgt"))):
                    hgt = int(fields.get("hgt").split("cm")[0])
                    if(hgt >= 150 and hgt <= 193):
                        hgtValid = True
                else:
                    hgt = int(fields.get("hgt").split("in")[0])
                    if(hgt >= 59 and hgt <= 76):
                        hgtValid = True

                if(byr >= 1920 and byr <= 2002
                    and iyr >= 2010 and iyr <= 2020
                    and eyr >= 2020 and eyr <= 2030
                    and hgtValid
                    and re.search("#[0-9a-f]{6}",fields.get("hcl"))
                    and re.search("amb|blu|brn|gry|grn|hzl|oth",fields.get("ecl"))
                    and len(fields.get("pid").rstrip()) == 9
                ):
                    count += 1  
            values = []
    print(count)

# part1()
part2()

file.close()