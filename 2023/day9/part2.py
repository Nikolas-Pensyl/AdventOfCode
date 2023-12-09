file = open("text.txt")
content = [[list(list(map(int, l.split())))] for l in file.readlines()]

nextVals = []
total = 0


for i in range(len(content)):
    #Get All difs to 0
    while not all([ x==0 for x in content[i][-1]]):
        content[i].append([content[i][-1][j+1] - content[i][-1][j] for j in range(len(content[i][-1])-1)])


    nextVal = 0
    for j in range(len(content[i])-1, -1, -1):
        nextVal = content[i][j][0] - nextVal

    nextVals.append(nextVal)
    total += nextVal

print(total)
