import re
file = open("input","r")
input = file.read().splitlines()

class op(int):
    def __mul__(self, x):
        return op(int(self) + x)
    def __add__(self, x):
        return op(int(self) + x)
    def __sub__(self, x):
        return op(int(self) * x)

def ev(expr,p2=False):
    expr = re.sub(r"(\d+)",r"op(\1)",expr)
    expr = expr.replace("*","-")
    if(p2):
        expr = expr.replace("+","*")
    return eval(expr,{},{"op":op})

def part1():
    return sum(ev(x) for x in input)

def part2():
    return sum(ev(x,p2=True) for x in input)

print("Part 1: ",part1())
print("Part 2: ",part2())

file.close()