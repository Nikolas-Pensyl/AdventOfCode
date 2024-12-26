from itertools import combinations

inp, gates = open('./Inputs/2024/day24.txt').read().split('\n\n')

ops = dict()

for line in gates.splitlines():
    a, o, b, _, c = line.split()

    ops[c] = (a, b, o)

def getWire(char, num):
    return char + str(num).rjust(2, "0")

def verify_carry_bit(wire, num):
    if wire[0] in 'xy': return False
    x, y, o = ops[wire]

    if num==1:
        if o!='AND': return False
        return sorted([x, y]) == ["x00", "y00"]
    
    if o!='OR': return False
    return (verify_direct_carry(x, num-1) and verify_recarry(y, num-1)) or (verify_direct_carry(y, num-1) and verify_recarry(x, num-1))
    

def verify_inter_xor(wire, num):
    if wire[0] in 'xy': return False
    x, y, o = ops[wire]

    if o!='XOR': return False

    return sorted([x, y]) == [getWire('x', num), getWire('y', num)]

def verify_direct_carry(wire, num):
    if wire[0] in 'xy': return False
    x, y, o = ops[wire]

    if o!='AND': return False
    return sorted([x, y]) == [getWire('x', num), getWire('y', num)]

def verify_recarry(wire, num):
    if wire[0] in 'xy': return False

    x, y, o = ops[wire]

    if o!='AND': return False
    return (verify_inter_xor(x, num) and verify_carry_bit(y, num)) or (verify_inter_xor(y, num) and verify_carry_bit(x, num))

def verify_z(num):
    wire = getWire('z', num)
    x, y, o = ops[wire]
    if o!='XOR': return False
    if num==0: return sorted([x, y]) == ['x00', 'y00']
    
    return (verify_inter_xor(x, num) and verify_carry_bit(y, num)) or (verify_inter_xor(y, num) and verify_carry_bit(x, num))

def progress():
    for i in range(46):
        if not verify_z(i):
            return i
        
    return 47

swaps = []
for _ in range(4):
    baseline = progress()
    for x in ops:
        if x in swaps: continue

        for y in ops:
            if x == y: continue
            if y in swaps: continue

            ops[x], ops[y] = ops[y], ops[x]
            if progress()>baseline:
                swaps.append(x)
                swaps.append(y)
                break
            ops[x], ops[y] = ops[y], ops[x]

        else: 
            continue
    
        break

print(swaps)