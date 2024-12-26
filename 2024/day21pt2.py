from functools import cache

data = [line for line in open('./Inputs/day21.txt').read().splitlines()]

keypad = {'0': (0, 1), 'A': (0, 2), '1': (1, 0), '2': (1, 1), '3':(1, 2), '4': (2, 0), '5': (2, 1), '6': (2, 2), '7': (3, 0), '8': (3, 1), '9': (3, 2)}
arrow = {'^': (1, 1), '<': (0, 0), 'v': (0, 1), '>': (0, 2), 'A': (1, 2)}

ar = [['<', 'v', '>'], ['', '^', 'A']]
keys = [['', '0', 'A'], ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]


@cache
def getPath(tar, curr, rob, npath):
    useArr = rob>0
    opt = ar if useArr else keys
    opts = arrow if useArr else keypad

    if tar==curr:
        npath +='A'

        if rob==25:
            return len(npath)

        count = 0
        c = 'A'
        for t in npath:
            count += getPath(t, c, rob+1, '')
            c = t

        return count
    

    cr, cc  = opts[curr][0], opts[curr][1]
    tr, tc = opts[tar][0], opts[tar][1]
    dr, dc = tr-cr, tc-cc

    lr = '<' if dc<0 else '>'
    ud = '^' if dr>0 else 'v'

    cPath = getPath(tar, opt[cr][cc+dc], rob, npath+lr*abs(dc)) if dc!=0 and opt[cr][cc+dc]!='' else 0 
    npath2 = getPath(tar, opt[dr+cr][cc], rob, npath+ud*abs(dr)) if dr!=0 and opt[dr+cr][cc]!='' else 0

    if cPath==0 or (npath2<cPath and npath2!=0):
        cPath = npath2

    return cPath



total = 0
for line in data:
    p = line
    curr = 'A'
    count = 0
    for t in line:
        count += getPath(t, curr, 0, '')
        curr = t
        
    print(count, int(line[:-1]))
    total += int(line[:-1])*count

print(total)