import copy
file = open("input","r")
input = file.read().split("\n\n")[:-1]
tiles = {}
for x in input:
    x = x.splitlines()
    tiles.update({ int(x[0][5:9]) : x[1:] })


def getEdges(t):
    t = tiles.get(t)
    left,right = [],[]
    for r in t:
        left.append(r[-1])
        right.append(r[0])
    return [list(t[0]),left,list(t[-1]),right]
    
edges = {}
for x in tiles:
    edges.update({ x : getEdges(x) })

def flipVertical(t):
    tr = copy.deepcopy(t)
    tr.reverse()
    return tr

def flipHorizontal(t):
    tr = copy.deepcopy(t)
    tnew = []
    for r in tr:
        r = r[::-1]
        tnew.append(r)
    return tnew

def rotateRight(t):
    l = len(t[0])
    tr = [[None for i in range(l)] for j in range(l)] 

    for ix,oldRow in enumerate(t):
        col = l - ix - 1
        for ir in range(l):
            tr[ir][col] = oldRow[ir]
    return tr

def trimTiles():
    for tid in tiles:
        t = tiles.get(tid)
        tr = []
        for r in t[1:-1]:
            tr.append(r[1:-1])
        tiles.update({ tid : tr })

def makeGrid(grid):
    g = []
    for row in grid:
        ts = [tiles.get(x) for x in row]
        for x in range(len(ts[0])):
            r = []
            for t in ts:
                r += t[x]
            g.append(r)
    return g

def matches1(x):
    tile1 = edges.get(x)
    m = 0

    for t1edge in tile1:
        for tile2 in tiles:
            t2edges = edges.get(tile2)
            if(x == tile2):
                continue
            for t2edge in t2edges:
                e2o = list(t2edge)
                t2edge.reverse()
                if(t1edge == e2o or t1edge == t2edge):
                    m += 1 

    return m == 2

def matches2(x):
    t1edges = edges.get(x)
    m = []

    for i1,t1edge in enumerate(t1edges):
        for tile2 in tiles:
            t2edges = edges.get(tile2)
            if(x == tile2):
                continue
            for i2,t2edge in enumerate(t2edges):
                e2o = list(t2edge)
                e2r = list(t2edge)
                e2r.reverse()
                if(t1edge == e2o):
                    m.append((i1,i2,tile2,False)) 
                elif(t1edge == e2r):
                    m.append((i1,i2,tile2,True))
    return m
        


def part1():
    s = 1
    for x in tiles:
        if(matches1(x)):
            s *= x
    return s


ran = {}
done = {}
def build(t):
    done.update({ t : True })
    matches = matches2(t)
    for m in matches:
        if(done.get(m[2])):
            continue

        tr = tiles.get(m[2])

        if(abs(m[0]) == abs(m[1])):
            if(m[0] % 2 == 0):
                tr = flipVertical(tr)
                if(m[3]):
                    tr = flipHorizontal(tr)
            else:
                tr = flipHorizontal(tr)
                if(m[3]):
                    tr = flipVertical(tr)
        else:
            if((m[0]+m[1]) % 2 == 1):
                if((not (m[0]==0 and m[1]==3)) and ( m[0]<m[1] or m[0]==3 and m[1]==0)):
                    tr = rotateRight(tr)
                    if(m[0]%2 == 0 and not m[3]):
                        tr = flipHorizontal(tr)
                    elif(m[0]%2 == 1 and m[3]):
                        tr = flipVertical(tr)

                else:
                    tr = rotateRight(tr)
                    tr = rotateRight(tr)
                    tr = rotateRight(tr)
                    if(m[0]%2 == 1 and not m[3]):
                        tr = flipVertical(tr)
                    elif(m[0]%2 == 0 and m[3]):
                        tr = flipHorizontal(tr)

            elif(m[3]):
                if(m[1] == 0 or m[1]==2):
                    tr = flipHorizontal(tr)
                else:
                    tr = flipVertical(tr)

        done.update({ m[2] : True })
        tiles.update({ m[2] : tr })
        edges.update({ m[2] : getEdges(m[2]) })

    for m in matches:
        if(len(done) == len(input)):
            return
        runtimes = ran.get(m[2]) if ran.get(m[2])!=None else 0
        ran.update({ m[2] : runtimes+1 })
        if(runtimes == 0):
            build(m[2])

    return


def part2():
    s = 0
    
    for tx in list(tiles.keys()):
        if(len(done) != len(input)):
            build(tx)

    matches = {}
    for x in tiles:
        matches.update({ x : matches2(x) })

    topLeft = None # Find topleft to start building grid from
    for x in matches:
        c = matches.get(x)
        if(len(c)==2 and c[0][0]==1 and c[1][0]==2 or c[0][0]==2 and c[1][0]==1):
            topLeft = x
            break
            
    grid = [[]]
    grid[0].append(topLeft)
    c = topLeft
    b = True
    while(b):
        b = False
        for x in matches.get(c):
            if(x[0] == 2):
                grid.append([x[2]])
                c = x[2]
                b = True

    for row in grid:
        c = row[0]
        b = True
        while(b):
            b = False
            for x in matches.get(c):
                if(x[0] == 1):
                    row.append(x[2])
                    c = x[2]
                    b = True
    trimTiles()
    g = makeGrid(grid)

    g.reverse() # Get right orientation for my specific puzzle
    g = rotateRight(g)

    strGrid = ""
    for r in g:
        strGrid += "".join(r) + "\n"

    points = [(0,18),(1,0),(1,5),(1,6),(1,11),(1,12),(1,17),(1,18),(1,19),(2,1),(2,4),(2,7),(2,10),(2,13),(2,16)]

    for y in range(len(g)-2):
        for x in range(len(g[0])-20):
            for d in points:
                if(g[y+d[0]][x+d[1]] != "#"):
                    break
            else:
                s += 1
    return strGrid.count("#") - s*15

print("Part 1: ",part1())
print("Part 2: ",part2())
file.close()