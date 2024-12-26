conns = {tuple(line.split('-')) for line in open('./Inputs/day23.txt').read().splitlines()}
nc = set()
comps = set()
for a, b in conns:
    comps.add(a)
    comps.add(b)
    nc.add((b, a))

conns = conns.union(nc)

cps = list(comps)

clen = len(comps)
count = 0
for i in range(clen):
    for j in range(i+1, clen):
        for k in range(j+1, clen):
            if (cps[i], cps[j]) in conns and (cps[j], cps[k]) in conns and (cps[i], cps[k]) in conns:
                if any('t'==cps[m][0] for m in (i, j, k)):
                    count +=1

print(count)
