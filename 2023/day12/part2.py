from collections import Counter
import multiprocessing

content = open('text.txt').read().strip().splitlines()
content = [[line.split()[0], list(map(int, line.split()[1].split(',')))] for line in content]

for i in range(len(content)):
    org = content[i][0]
    orgNum = content[i][1].copy()
    for j in range(4):
        content[i][0] += '?'+org
        content[i][1] += orgNum


def verify(input, hash):
    hashArr = [len(x) for x in input.split('.') if len(x)>0]
    if len(hashArr) != len(hash):
        return False
    return all([hashArr[i] == hash[i] for i in range(len(hash))])

def verifyPartial(input, hash, index):
    currHash = 0
    hashIndex = 0
    hashSum = sum(hash)
    count = Counter(input)

    if count['#'] > hashSum or hashSum > count['#']+count['?']:
        return False

    for i in range(index+1):
        if input[i] == '#' and currHash ==0 and i!=0 and input[i-1] != '.':
            return False

        elif input[i] == '#':
            if len(hash) == hashIndex: 
                return False
            currHash +=1
            if currHash == hash[hashIndex]:
                if i+1!=len(input) and input[i+1] == '#':
                    return False
                else:
                    currHash = 0
                    hashIndex +=1

        elif input[i] == '.' and hashIndex<len(hash) and currHash>0:
            return False

    return True


def getCombos(input, hash, results, resIndex):
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
                if verifyPartial(arragements[j], hash, i):
                    arragements.insert(0, arragements[j])
                    j +=1

                arragements[j] = arragements[j][:i] + '.' + arragements[j][addEnding:]
                if not verifyPartial(arragements[j], hash, i):
                    arragements.pop(j)
                    j -=1
                
            j +=1
    
        i +=1
    
    count = 0
    for i in arragements:
        if verify(i, hash):
            count += 1
    results[resIndex] = count
    print(resIndex)
    return count


total = 0
results = [0 for i in range(len(content))]
threads = [None for i in range(len(content))]
'''
for i, line in enumerate(content):
    print(i)
    total += getCombos(line[0], line[1], results, i)
'''

for i, line in enumerate(content):
    threads[i] = multiprocessing.Process(target = getCombos, args=(line[0], line[1], results, i))
    threads[i].start()


for i in range(len(threads)):
    threads[i].join()

print(sum(results))
