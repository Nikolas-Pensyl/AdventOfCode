file = open("text.txt")
content = [[pattern.split('\n')] for pattern in file.read().split('\n\n')]

#Probably a better way to transpose the string and matrix
for i in range(len(content)):
    pattern = content[i][0]
    tranContent = []
    for j in range(len(pattern[0])):
        tranString = ''
        for k in range(len(pattern)):
            tranString += pattern[k][j]
        tranContent.append(tranString)
    content[i].append(tranContent)

def isOffByOne(comp1, comp2):
    diff = False
    for i in range(len(comp1)):
        if comp1[i] != comp2[i]:
            if diff:
                return False
            diff = True
    return diff

#We love recursion
def getIsMirror(contentDict, offByOne, pattern, j, useOffBy, count, start):
    if j-(count*2+1) == 0 or j >= len(pattern)-1: return start if useOffBy else -1
    
    j += 1
    count +=1

    if j-(count*2+1) in contentDict[pattern[j]]:
        num = getIsMirror(contentDict, offByOne, pattern, j, useOffBy, count, start)
        if num!=-1:
            return num
    
    if j-(count*2+1) in offByOne[j] and not useOffBy:
        return getIsMirror(contentDict, offByOne, pattern, j, True, count, start)

    return -1


def getMirrorLoc(patterns, i):
    contentDict = [{}, {}]
    offByOne = [{}, {}]

    #Get Pairs and Off by one Pairs
    for k in range(len(patterns)):
        pattern = patterns[k]
        for j in range(len(pattern)):
            offByOne[k][j] = []

        for j in range(len(pattern)):
            line = pattern[j]
            lineNum = contentDict[k].get(line, -1)

            if lineNum!=-1:
                contentDict[k][line] = (j, *lineNum)
            else:
                contentDict[k][line] = (j,)
            for m in range(j+1, len(pattern)):
                if m != j and isOffByOne(pattern[m], pattern[j]):
                    offByOne[k][m].append(j)
                    offByOne[k][j].append(m)

        #Check if pairs there is a match with one off
        start = -1
        for j in range(1, len(pattern)):
            line = pattern[j]
            lineNum = contentDict[k].get(line, [])

            if j-1 in lineNum:
                start = getIsMirror(contentDict[k], offByOne[k], pattern, j, False, 0, j)

            if j-1 in offByOne[k][j]:
                start = getIsMirror(contentDict[k], offByOne[k], pattern, j, True, 0, j)
            
            if start != -1:
                break
    
        if start != -1:
            #If Horizontal match multiply by 100
            if k==0:
                start *=100
            return start
    return 0


total = 0
for i, pattern in enumerate(content):
    total += getMirrorLoc(pattern, i)


print(total)
