map, moves = open('./Inputs/day15.txt').read().split('\n\n')

moves = "".join(line.strip() for line in moves)
map = map.splitlines()

rob = [0, 0]
boxes = set()
walls = set()

dirs = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v':(1, 0)}

for r, line in enumerate(map):
    for c, ch in enumerate(line):
        if ch =='#':
            walls.add((r, c))
        
        if ch == 'O':
            boxes.add((r, c))

        if ch=='@':
            rob = [r, c]

def isValid(rr, rc, dr, dc, isBox=False):
    nr, nc = rr+dr, rc+dc
    if (nr, nc) in walls:
        return False
    
    if (nr, nc) not in boxes:
        if isBox:
            boxes.remove((rr, rc))
            boxes.add((nr, nc))

        return True
    
    #If in Boxes 
    if isValid(nr, nc, dr, dc, True):
        if isBox:
            boxes.remove((rr, rc))
            boxes.add((nr, nc))

        return True

    return False

for m in moves:
    dr, dc = dirs[m]
    nr, nc = rob[0]+dr, rob[1]+dc
    if isValid(rob[0], rob[1], dr, dc, False):
        rob = [nr, nc]

total = 0
for br, bc in boxes:
    total += (br*100)+bc

print(total)
'''for r in range(len(map)):
    st = ""
    for c in range(len(map[0])):
        st += "O" if (r, c) in boxes else "#" if (r, c) in walls else "@" if rob[0]==r and rob[1]==c else "."
    
    print(st)'''