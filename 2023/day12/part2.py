import copy

content = open('text.txt').read().strip().splitlines()
content = [[line.split()[0], list(map(int, line.split()[1].split(',')))] for line in content]


for i in range(len(content)):
    org = content[i][0]
    orgNum = content[i][1].copy()
    for j in range(4):
        content[i][0] += '?'+org
        content[i][1] += orgNum
    break


def verify(input, hash):
    currHash = 0
    hashIndex = 0
    for i, char in enumerate(input):
        if char == '#' and currHash ==0 and i!=0 and input[i-1] != '.':
            return False
        elif char == '#':
            if len(hash) == hashIndex: 
                return False
            currHash +=1
            if currHash == hash[hashIndex]:
                if i+1!=len(input) and input[i+1] != '.':
                    return False
                else:
                    currHash = 0
                    hashIndex +=1

        if char == '.' and hashIndex<len(hash) and currHash != hash[hashIndex] and currHash>0:
            return False

    return True if hashIndex == len(hash) else False


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
    break

print(total)
