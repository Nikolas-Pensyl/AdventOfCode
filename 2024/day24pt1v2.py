inp, gates = open('./Inputs/2024/day24.txt').read().split('\n\n')

ops = dict()
vals = dict()
ready = set()

for i in inp.splitlines():
    a, b = i.split(': ')
    vals[a] = int(b)

for line in gates.splitlines():
    a, o, b, _, c = line.split()

    ops[c] = (a, b, o)


def calc(wire):
    if wire in vals:
        return vals[wire]
    
    a, b, o = ops[wire]

    if o=='AND': 
        vals[wire] = calc(a)&calc(b)
    elif o=='XOR':
        vals[wire] = calc(a)^calc(b)
    else: 
        vals[wire] = calc(a)|calc(b)

    return vals[wire]

v = 0
for i in range(46):
    nz = 'z'+ str(i) if i>=10 else 'z0' + str(i)
    v += calc(nz)<<i

print(v)