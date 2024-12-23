conns = {tuple(line.split('-')) for line in open('./Inputs/day23t.txt').read().splitlines()}
cdict: dict[str, list] = dict()
comps = set()

#Make a set of computers and a dictationary of a list of connected computers
for a, b in conns:
    if a not in comps:
        cdict[a] = []

    if b not in comps:
        cdict[b] = []

    cdict[a].append(b)
    cdict[b].append(a)

    comps.add(a)
    comps.add(b)

maxl = 0
st= ''

#Make every computer a host
#Loop through all connected computers to the host
#Add to list if all the computers in the list are connectde to the candidate
for host in comps:
    cps = cdict[host]
    cml = {host}

    for c in cps:
        if all(k in cdict[c] for k in cml):
            cml.add(c)
    
    if len(cml)>maxl:
        maxl = len(cml)
        st = ','.join(sorted(list(cml)))

print(st)
