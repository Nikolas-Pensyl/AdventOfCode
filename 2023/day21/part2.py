content = open("text.txt").read().splitlines()


#Get StartPos
startPos = ()
for y, line in enumerate(content):
    for x, char in enumerate(line):
        if char == 'S':
            startPos = (x, y)


#Lengths
lenX = len(content[0])
lenY = len(content)
steps = 26501365

def getNum(maxStep = lenX, startX = startPos[0], startY = startPos[1]):
    global lenX, lenY

    #Get Total for one board Odds
    moves = [(startX, startY, maxStep)]
    seen = {(startX, startY)}
    completed = set()
    while moves:
        x, y, n = moves.pop(0)

        if n %2 == 0:
            completed.add((x, y))
        
        if n == 0:
            continue
        
        for xs, ys in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = x+xs
            ny = y+ys
            if -1<nx<lenX and -1<ny<lenY and content[ny][nx] != '#' and (nx, ny) not in seen:
                seen.add((nx, ny))
                moves.append((nx, ny, n-1))
    
    return len(completed)



odd = getNum(lenX*2+1)
even = getNum(lenX*2)

top = getNum(lenX-1, lenX//2, lenY-1)
bottom = getNum(lenX-1, lenX//2, 0)
left = getNum(lenX-1, lenX-1, lenY//2)
right = getNum(lenX-1, 0, lenY//2)

small_tr = getNum(lenX//2-1, 0, lenX-1)
small_tl = getNum(lenX//2-1, lenX-1, lenX-1)
small_br = getNum(lenX//2-1, 0, 0)
small_bl = getNum(lenX//2-1, lenX-1, 0)

large_tr = getNum(lenX*3//2-1, 0, lenX-1)
large_tl = getNum(lenX*3//2-1, lenX-1, lenX-1)
large_br = getNum(lenX*3//2-1, 0, 0)
large_bl = getNum(lenX*3//2-1, lenX-1, 0)

grid_width = (steps//lenX) -1
oddGrids = (grid_width // 2 * 2 + 1) ** 2
evenGrids = ((grid_width + 1) // 2 * 2) ** 2

print(oddGrids * odd + evenGrids * even + (grid_width+1)*(small_tr+small_bl+small_br+small_tl) + (grid_width) *(large_bl+large_br+large_tl+large_tr) + top + left + right + bottom)
