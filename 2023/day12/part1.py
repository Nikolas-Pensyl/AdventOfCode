import copy

content = open('text.txt').read().strip().splitlines()
content = [[line.split()[0], list(map(int, line.split()[1].split(',')))] for line in content]

def verify(input, hash):
    hashArr = [len(x) for x in input.split('.') if len(x)>0]
    if len(hashArr) != len(hash):
        return False
    return all([hashArr[i] == hash[i] for i in range(len(hash))])


def getCombos(input, hash):
    lengthIn = len(input)
    arragements = []
    arragements.append(input)
    i=0
    while i<lengthIn:
        j=0
        while j<len(arragements):
            if arragements[j][i] == '?':
                addEnding = i+1 if i+1 !=lengthIn else lengthIn
                arragements[j] = arragements[j][:i] + '#' + arragements[j][addEnding:]
                arragements.insert(0, arragements[j])
                j +=1
                arragements[j] = arragements[j][:i] + '.' + arragements[j][addEnding:]
            j +=1
    
        i +=1
    
    count = 0
    for i in arragements:
        if verify(i, hash):
            count += 1
    
    return count


total = 0
for i, line in enumerate(content):
    total += getCombos(line[0], line[1])

print(total)
