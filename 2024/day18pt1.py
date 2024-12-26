data = tuple(tuple(map(int, line.split(','))) for i, line in enumerate(open('./Inputs/day18.txt').read().splitlines()))


dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
start = (0, 0)
ma = 70
#end = (70, 70)

end = (ma, ma)
def getPath(k):
    visited = {(0, 0)}
    paths = [(0, 0, 0, set())]
    e=False
    while len(paths)>0:
        x, y, s, p = paths.pop(0)
        p.add((x, y))

        for dx, dy in dirs:
            ny, nx = y+dy, x+dx
            if (nx, ny) in visited or 0>ny or ma<ny or 0>nx or ma<nx or (nx, ny) in data[:k]: continue
            
            if (nx, ny)==end:
                return p
            
            visited.add((nx, ny))
            paths.append((nx, ny, s+1, p.copy()))

    return {}


for k in range(len(data), 0, -1):
    pa = getPath(k)
    if len(pa)!=0:
        print(data[k])
        break

exit()
for r in range(71):
    s = ""
    for c in range(71):
        if (r, c) in data:
            s += '#'
        elif (r, c) in visited:
            s += 'O'
        else: s+='.'
    
    print(s)