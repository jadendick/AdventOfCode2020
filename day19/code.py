import re
file = open("input","r")
input = file.read().split("\n\n")
ruleInput = input[0].split("\n")
i2 = input[1].split("\n")[:-1]

done = {}
rules = {}
for r in ruleInput:
    parts = r.split(": ")
    rules.update({ parts[0] : parts[1] })

def makeRule(r,p2):
    rule = rules.get(r)
        
    match = ""
    if(done.get(r)):
        match = rules.get(r)

    elif(p2 and r == "8"):
        match = "("+makeRule("42",p2)+")+"
        
    elif(p2 and r == "11"):
        match = "("+makeRule("42",p2)+")#("+makeRule("31",p2)+")#"
        match = re.sub("#","",match)+"|"+re.sub("#","{1}",match)+"|"+re.sub("#","{2}",match)+"|"+re.sub("#","{3}",match)+"|"+re.sub("#","{4}",match)
        
    elif("\"" in rule):
        rules.update({ r : rule[-2] })
        done.update({ r : True })
        return rule[-2]

    elif("|" in rule):
        split = rule.split(" | ")
        for x in split[0].split(" "):
            match += makeRule(x,p2)
        match += "|"
        for x in split[1].split(" "):
            match += makeRule(x,p2)

    else:
        for x in rule.split(" "):
            match += makeRule(x,p2)

    done.update({ r : True })
    rules.update({ r : match })
    
    return match if len(match)==1 else "("+match+")"

        

def part1(p2):
    s = 0
    rule = makeRule("0",p2)

    for x in i2:
        if(re.fullmatch(rule,x)):
            s += 1

    return s

print(part1(False)) # Pass True to run part 2
# print(part1(True)) # Pass True to run part 2

file.close()