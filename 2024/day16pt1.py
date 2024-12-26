from heapq import heappop, heappush

data = [[ch for ch in line] for line in open('./Inputs/day16.txt').read().splitlines()]

dirs = {(1, 0), (-1, 0), (0, 1), (0, -1)}

rows = len(data)
cols = len(data[0])

start = (0, 0)
end = (0, 0)
for r, line in enumerate(data):
    for c, ch in enumerate(line):
        if ch == 'S':
            start = (r, c)

        if ch=='E':
            end = (r, c)


visited = set()
spots = set()
minScore = -1
sr, sc = start

opts = [(0, sr, sc, 0, 1)]
maxSc = float("inf")
while len(opts)!=0:
    score, r, c, dr, dc= heappop(opts)
    visited.add((r, c))
    if score>maxSc: break
    
    #Rob in spots Trail off or something
    if (r, c)==end:
        maxSc = score
        print(maxSc)
        break
    
    for ndr, ndc in dirs:
        nr, nc = r+ndr, c+ndc
        if 0>nr or rows<=nr or 0>nc or cols<=nc: continue
        if data[nr][nc] =='#': continue
        if (nr, nc) in visited: continue

        ns = score+1
        if dr!=ndr or dc!=ndc: ns+=1000
        
        heappush(opts, (ns, nr, nc, ndr, ndc))

#print(len(spots))
