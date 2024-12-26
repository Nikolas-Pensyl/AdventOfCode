inp, gates = open('./Inputs/2024/day24.txt').read().split('\n\n')

ops = dict()
vals = dict()
ready = set()

for i in inp.splitlines():
    a, b = i.split(': ')
    vals[a] = int(b)

    ready.add(a)

for line in gates.splitlines():
    
    a, o, b, _, c = line.split()

    ops[c] = (a, b, o)

while len(ops)>0:
    rem = set()

    for c in ops.keys():

        a, b, o = ops[c]
        if a not in ready or b not in ready: continue
        
        if o=='AND': 
            vals[c] = vals[a]&vals[b]
        elif o=='XOR':
            vals[c] = vals[a]^vals[b]
        else: 
            vals[c] = vals[a]|vals[b]

        ready.add(c)
        rem.add(c)

    for t in rem:
        ops.pop(t)

c = 0
v = 0
for i in range(46):
    v += vals['z'+ str(i) if i>=10 else 'z0' + str(i)]<<i

print(v)