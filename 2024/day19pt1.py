towels, combos = open('./Inputs/day19.txt').read().split('\n\n')

towels = towels.split(', ')
combos = combos.splitlines()

maxLen = max([len(t) for t in towels])
minLen = min([len(t) for t in towels])


seen = dict()
def getRem(rem):
    if len(rem)==0:
        return 1

    if rem in seen:
        return seen[rem]
    
    total = 0 

    rlen = len(rem)
    for i in range(minLen, min(rlen+1, maxLen+1)):
        if rem[:i] in towels: 
            total += getRem(rem[i:])

    seen[rem] = total
    return total
    
    

count = 0
for k, cb in enumerate(combos):
    count += getRem(cb)

print(count)


