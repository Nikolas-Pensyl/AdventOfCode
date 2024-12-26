data = list(map(int, open('./Inputs/day22.txt').read().splitlines()))

total = 0

for n in data:
    r = n
    for i in range(2000):
        r ^= r<<6
        r &= 16777215
        r ^= r>>5
        r &= 16777215
        r ^= r<<11
        r &= 16777215

    total +=r

print(total)
