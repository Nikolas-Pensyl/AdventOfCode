from heapq import heappop, heappush

data = [line for line in open('./Inputs/day21.txt').read().splitlines()]

keypad = {'0': (0, 1), 'A': (0, 2), '1': (1, 0), '2': (1, 1), '3':(1, 2), '4': (2, 0), '5': (2, 1), '6': (2, 2), '7': (3, 0), '8': (3, 1), '9': (3, 2)}
arrow = {'^': (1, 1), '<': (0, 0), 'v': (0, 1), '>': (0, 2), 'A': (1, 2)}

ar = [['<', 'v', '>'], ['', '^', 'A']]
keys = [['', '0', 'A'], ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]


total = 0
for line in data:
    sps = {line}
    rob = 0

    while rob!=3:
        #count of button presses, robot number, new path, index of target path, curr, target path
        hp = [(0, rob, '', 0, 'A', s) for s in sps]
        sps = set()
        useArr = rob>0
        opt = ar if useArr else keys
        opts = arrow if useArr else keypad
        maxCount = float("inf")
        while len(hp)!=0:
            count, robn, npath, ind, curr, tpath = heappop(hp)

            if maxCount<count:
                break

            if ind==len(tpath):
                sps.add(npath)
                maxCount = count
                if rob == 2:
                    break
                continue
            
            t = tpath[ind]

            cr, cc  = opts[curr][0], opts[curr][1]
            tr, tc = opts[t][0], opts[t][1]
            dr, dc = tr-cr, tc-cc
            
            if curr == t: 
                heappush(hp, (count+1, robn, npath+'A', ind+1, t, tpath))

            #Going right is always safe
            if dc>0 and opt[cr][cc+dc]!='': 
                heappush(hp, (count+abs(dc), robn, npath+'>'*abs(dc), ind, opt[cr][cc+dc], tpath))

            #If we need to go up and we are not using the arrow keys or we are not under the blank spot of the arrow key
            if dr>0 and opt[cr+dr][cc]!='': 
                heappush(hp, (count+abs(dr), robn, npath+'^'*abs(dr), ind, opt[cr+dr][cc], tpath))

            # If we need to go down and we are using the arrow keys or we are not going down to zero or not in column zero 
            if dr<0 and opt[cr+dr][cc]!='': 
                heappush(hp, (count+abs(dr), robn, npath+'v'*abs(dr), ind, opt[cr+dr][cc], tpath))
            
            #If we need to go left and we are not going into a blank zone for either the arrow keys or the numpad
            if dc<0 and opt[cr][cc+dc]!='': 
                heappush(hp, (count+abs(dc), robn, npath+'<'*abs(dc), ind, opt[cr][cc+dc], tpath))

            
        rob +=1

    total += int(line[:-1])*max(len(p) for p in sps)

print(total)