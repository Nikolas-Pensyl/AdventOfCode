from itertools import combinations

inp, gates = open('./Inputs/2024/day24.txt').read().split('\n\n')

ops = dict()
vals = dict()

xs = 0
ys = 0
for i in inp.splitlines():
    a, b = i.split(': ')
    vals[a] = int(b)

for i in range(45):
    xs += vals['x'+ str(i) if i>=10 else 'x0' + str(i)]<<i
    ys += vals['y'+ str(i) if i>=10 else 'y0' + str(i)]<<i

goalSum = xs+ys

for line in gates.splitlines():
    a, o, b, _, c = line.split()

    ops[c] = (a, b, o)

def pp(wire, depth=0):
    if wire[0] in 'xy': return ' '+str(vals[wire])
    st = ""
    a, b, o = ops[wire]
    st += ' '*depth+f'{a} {o} {b} \n ' 
    st += ' '*(depth+1) + f'{a} {pp(a, depth+1)}\n '
    st += ' '*(depth+1) + f'{b} {pp(b, depth+1)}\n'
    return st

c = 0
v = 0
for i in range(45, -1, -1):
    #v += vals['z'+ str(i) if i>=10 else 'z0' + str(i)]<<i
    print('z'+ str(i)+'\n' if i>=10 else 'z0' + str(i)+'\n', pp('z'+ str(i) if i>=10 else 'z0' + str(i)))
    exit()



if v==goalSum:
    print('Done')

print(v)