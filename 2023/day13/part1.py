file = open("text.txt")
content = [[pattern.split('\n')] for pattern in file.read().split('\n\n')]


for i in range(len(content)):
    pattern = content[i][0]
    tranContent = []
    for j in range(len(pattern[0])):
        tranString = ''
        for k in range(len(pattern)):
            tranString += pattern[k][j]
        tranContent.append(tranString)
    content[i].append(tranContent)

def getMirrorLoc(patterns, i):
    contentDict = [{}, {}]
    for k in range(len(patterns)):
        pattern = patterns[k]
        isMirror = False
        end = False
        count = 0
        start = 0
        for j in range(len(pattern)):
            line = pattern[j]
            lineNum = contentDict[k].get(line, -1)

            if lineNum!=-1:
                contentDict[k][line] = (j, *lineNum)
                if not isMirror and j-1 in lineNum:
                    isMirror = True
                    count +=1
                    start = j
                    if j-1 == 0:
                        end = True
                        break
                elif isMirror:
                    if j-(count*2+1) in lineNum and not end:
                        if j-(count*2+1) == 0 or j == len(pattern)-1:
                            end = True
                            break
                        else:
                            count +=1
                    elif not end:
                        isMirror = False

                    
           
            elif not end:
                contentDict[k][line] = (j,)
                isMirror = False
                count = 0
    
        if isMirror:
            if k==0:
                start *=100
            return start
    print(i)
    return 0


total = 0
for i, pattern in enumerate(content):
    total += getMirrorLoc(pattern, i)

print(total)
