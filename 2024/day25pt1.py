data = [line.splitlines() for line in open('./Inputs/2024/day25.txt').read().split('\n\n')]

k = set()
l = set()

for o in data:
    if o[0][0]=='#':
        l.add(tuple(sum(o[r][c]=='#' for r in range(len(o)))-1 for c in range(len(o[0]))))
    else:
        k.add(tuple(sum(o[r][c]=='#' for r in range(len(o)))-1 for c in range(len(o[0]))))


total = 0
for lock in l:
    for key in k:
        if all(lock[i]+key[i]<=5 for i in range(len(lock))):
            total +=1

print(total)