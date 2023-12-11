file = open("text.txt")
content = file.readlines()
content = [[content[i][j] for j in range(len(content[i])) if content[i][j] != '\n'] for i in range(len(content))]
isEmptyRows = [all([content[i][j] == '.' for j in range(len(content[i]))]) for i in range(len(content))]
isEmptyCols = [all([content[i][j] == '.' for i in range(len(content))]) for j in range(len(content[0]))]


NodeLocs = []
numEmptyRows = 0
numEmptyCols = 0
for i in range(len(content)):
    numEmptyCols = 0
    if isEmptyRows[i]: numEmptyRows +=1
    for j in range(len(content[i])):
        if isEmptyCols[j]: numEmptyCols +=1
        if content[i][j] == '#':
            NodeLocs.append([j+numEmptyCols*999999, i+numEmptyRows*999999])


total = 0
for i in range(len(NodeLocs)-1):
    for j in range(i+1, len(NodeLocs)):
        total += abs(NodeLocs[i][1]-NodeLocs[j][1]) + abs(NodeLocs[i][0]-NodeLocs[j][0])

print(total)
