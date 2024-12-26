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
back = dict()
visSc = dict()

sr, sc = start

opts = [(0, sr, sc, 0, 1)]
maxSc = float("inf")
visSc[(sr, sc, 0, 1)] = 0
back[(sr, sc, 0, 1)] = set()
while len(opts)!=0:
    score, r, c, dr, dc= heappop(opts)

    if visSc[(r, c, dr, dc)]<score: continue

    if score>maxSc: break
    
    #Rob in spots Trail off or something
    if (r, c)==end:
        maxSc = score
        continue
    
    for ndr, ndc in dirs:
        nr, nc = r+ndr, c+ndc
        if 0>nr or rows<=nr or 0>nc or cols<=nc: continue
        if data[nr][nc] =='#': continue

        ns = score+1
        if dr!=ndr or dc!=ndc: ns+=1000
        
        if visSc.get((nr, nc, ndr, ndc), float("inf"))>ns:
            visSc[(nr, nc, ndr, ndc)] = ns
            back[(nr, nc, ndr, ndc)] = set()

        if visSc[(nr, nc, ndr, ndc)]<ns: continue

        back[(nr, nc, ndr, ndc)].add((r, c, dr, dc))

        heappush(opts, (ns, nr, nc, ndr, ndc))


seen = set([(end[0], end[1], dr, dc) for dr, dc in dirs if (end[0], end[1], dr, dc) in visSc])
track = [(end[0], end[1], dr, dc) for dr, dc in dirs if (end[0], end[1], dr, dc) in visSc]
while len(track)!=0:
    t = track.pop(0)
    o = back[t]
    for n in o:
        if n not in seen:
            seen.add(n)
            track.append(n)

coord_seen = set([(n[0], n[1]) for n in seen])
print(len(coord_seen))