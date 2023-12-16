content = open("text.txt").read().strip().splitlines()



#dir: 0 = up, 1 = right, 2 = down, 3 = left
routes = []
traversed = set({})
def travel(y, x, dir):
    char = content[y][x]
    
    if dir == 0:
        if char in '.|':
            return [y-1, x, dir]
        elif char == '-':
            routes.append([y, x-1, 3])
            return [y, x+1, 1]
        elif char=='\\':
            return [y, x-1, 3]
        elif char == '/':
            return [y, x+1, 1]
    elif dir == 2:
        if char in '.|':
            return [y+1, x, dir]
        elif char == '-':
            routes.append([y, x-1, 3])
            return [y, x+1, 1]
        elif char=='\\':
            return [y, x+1, 1]
        elif char == '/':
            return [y, x-1, 3]
    if dir == 1:
        if char in '.-':
            return [y, x+1, dir]
        elif char == '|':
            routes.append([y+1, x, 2])
            return [y-1, x, 0]
        elif char=='\\':
            return [y+1, x, 2]
        elif char == '/':
            return [y-1, x, 0]
    elif dir == 3:
        if char in '.-':
            return [y, x-1, dir]
        elif char == '|':
            routes.append([y-1, x, 0])
            return [y+1, x, 2]
        elif char=='\\':
            return [y-1, x, 0]
        elif char == '/':
            return [y+1, x, 2]
    
    return

startingRoutes = []
for i in range(len(content)):
    startingRoutes.append([i, 0, 1])
    startingRoutes.append([i, len(content[0])-1, 3])

for i in range(len(content[0])):
    startingRoutes.append([len(content)-1, i, 0])
    startingRoutes.append([0, i, 2])

energized = [[[False for char in line] for line in content] for k in range(len(startingRoutes))]
maxVal = 0
count = 0
while len(startingRoutes)>count:
    routes.append(startingRoutes[count])
    traversed = set({})
    while len(routes)>0:
        y, x, dir = routes.pop(0)
        while -1<x<len(content[0]) and -1<y<len(content) and (x, y, dir) not in traversed:
            traversed.add((x, y, dir))
            energized[count][y][x] = True
            y, x, dir = travel(y, x, dir)
        val = sum([sum([1 if x else 0 for x in y]) for y in energized[count]])
        if maxVal<val:
            maxVal = val
    count +=1

print(maxVal)
