file = open("text.txt")
content = file.readlines()
content = [[content[i][j] for j in range(len(content[i])) if content[i][j] != '\n'] for i in range(len(content))]

i=0
while i<len(content):
    isEmpty = True
    for j in range(len(content[i])):
        if content[i][j] == '#':
            isEmpty = False
            break
    if isEmpty:
        print(i)
        content.insert(i, content[i])
        i +=1
    i+=1

j=0
while j<len(content[0]):
    isEmpty = True
    for i in range(len(content)):
        if content[i][j] == '#':
            isEmpty = False
            break
    if isEmpty:
        for i in range(len(content)):
            content[i].insert(j, '.')
        j +=1
    j +=1


NodeLocs = []
for i in range(len(content)):
    for j in range(len(content[i])):
        if content[i][j] == '#':
            NodeLocs.append([j, i])


total = 0
for i in range(len(NodeLocs)-1):
    for j in range(i+1, len(NodeLocs)):
        total += abs(NodeLocs[i][1]-NodeLocs[j][1]) + abs(NodeLocs[i][0]-NodeLocs[j][0])

print(total)
