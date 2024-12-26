data = list(map(int, open('./Inputs/day22.txt').read().splitlines()))

sequences: dict[tuple, int] = dict()
maxBanana = 0
for ind, n in enumerate(data):
    seqs = set()
    r = n
    changes = []
    ndig = r%10
    for i in range(2000):
        dig = ndig

        r ^= r<<6
        r &= 16777215
        r ^= r>>5
        r &= 16777215
        r ^= r<<11
        r &= 16777215
        
        ndig = r%10
        changes.append(ndig-dig)
        if i>=3:
            chseq = tuple(changes)
            if chseq not in seqs:
                seqs.add(chseq)
                nval = sequences.get(chseq, 0) + ndig
                sequences[chseq] = nval
                maxBanana = max(maxBanana, nval)
        
            changes.pop(0)

print(maxBanana)