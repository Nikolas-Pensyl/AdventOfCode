map, moves = open('./Inputs/day15.txt').read().split('\n\n')

moves = "".join(line.strip() for line in moves)
map = map.splitlines()

rob = [0, 0]
boxes = set()
walls = set()

dirs = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v':(1, 0)}
bd: dict[tuple, tuple] = dict()

#Get Boxes and Walls and Robot
for r, line in enumerate(map):
    for c, ch in enumerate(line):
        if ch =='#':
            walls.add((r, c*2))
            walls.add((r, c*2+1))
        
        if ch == 'O':
            bd[(r, c*2)] = (r, c*2+1)
            bd[(r, c*2+1)] = (r, c*2)

        if ch=='@':
            rob = [r, c*2]


rem = set()
addd = dict()
#Check if next position is valid
def isValid(r, c, dr, dc, bs=False):
    nr, nc = r+dr, c+dc
    if (nr, nc) in walls:
        return False
    

    if (nr, nc) not in bd.keys(): 
        if bs:
            otr, otc = bd[(r, c)]
            rem.add((r, c))
            rem.add((otr, otc))

            addd[(otr+dr, otc+dc)] = (nr, nc)
            addd[(nr, nc)] = (otr+dr, otc+dc)

        return True
    
    
    if dr!=0:
        otr, otc = bd[(nr, nc)]
        if isValid(nr, nc, dr, dc, True) and isValid(otr, otc, dr, dc, True):
            if bs:
                otr, otc = bd[(r, c)]
                rem.add((r, c))
                rem.add((otr, otc))

                addd[(otr+dr, otc+dc)] = (nr, nc)
                addd[(nr, nc)] = (otr+dr, otc+dc)
            
            return True

    if dc!=0:
        otr, otc = bd[(nr, nc)]
        if isValid(otr, otc, dr, dc, True):
            if bs:
                otr, otc = bd[(r, c)]
                rem.add((r, c))
                rem.add((otr, otc))

                addd[(otr+dr, otc+dc)] = (nr, nc)
                addd[(nr, nc)] = (otr+dr, otc+dc)

            return True
    
    return False

#Loop through all of the moves
for m in moves:
    dr, dc = dirs[m]
    nr, nc = rob[0]+dr, rob[1]+dc
    rem = set()
    addd = dict()
    if isValid(rob[0], rob[1], dr, dc, False):
        for b in rem:
            bd.pop(b)
        
        for k in addd.keys():
            bd[k] = addd[k]

        rob = [nr, nc]

        

#Get the total of the boxes
total = 0
for br, bc in bd.keys():
    otr, otc = bd[(br, bc)]
    if otc+1==bc: continue
    total += (br*100)+bc

print(total)

