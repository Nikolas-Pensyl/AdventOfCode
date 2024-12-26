data = [[ch for ch in line] for line in open('./Inputs/day20.txt').read().splitlines()]

rows = len(data)
cols = len(data[0])
start = (0, 0)
end = (0, 0)

dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))

#Get start and end
for r in range(rows):
    for c in range(cols):
        if data[r][c]=='S':
            start = (r, c)

        if data[r][c]=='E':
            end = (r, c)

#Get Path
path = []
pr, pc = start
count = 0
while (pr, pc)!=end:
    path.append((pr, pc))
    count +=1
    for dr, dc in dirs:
        nr, nc = pr+dr, pc+dc
        if 0>nr or rows<=nr or 0>nc or cols<=nc: continue
        if data[nr][nc]=='#': continue

        if count<2 and (nr, nc) in path: continue
        if count>=2 and path[-2]==(nr, nc): continue

        pr, pc = nr, nc
        break

path.append(end)

cheats = set()
#Get Cheats
for ind, p in enumerate(path):
    sr, sc = p
    for dr, dc in dirs:
        nr, nc = sr+dr, sc+dc
        nnr, nnc = nr+dr, nc+dc

        if 0>nnr or rows<=nnr or 0>nnc or cols<=nnc: continue
        if data[nr][nc]!='#' or data[nnr][nnc]=='#': continue

        nind = path.index((nnr, nnc))

        t = nind-ind-2
        if t>=100:
            cheats.add((nr, nc, nnr, nnc))

print(len(cheats))