file = open("text.txt")
content = file.readlines()
content = [[j for j in content[i] if j != '\n'] for i in range(len(content))]
start = [-1, -1]
stepMap = [[0 for i in range(len(content[0]))] for j in range(len(content))]
stepNum = 0

possibleLeft = 'LF-'
possibleRight = 'J7-'
possibleUp = '|7F'
possibleDown = 'JL|'

#[x, y, PrevX, PrevY]
currLoc = [[0, 0, -1, -1], [0, 0, -1, -1]]


def isPrevLoc(x0, y0, x1, y1):
    return x0 == x1 and y0 == y1

def setPrevLoc(i):
    currLoc[i][2] = currLoc[i][0]
    currLoc[i][3] = currLoc[i][1]

for i in range(len(content)):
    for j in range(len(content[i])):
        if content[i][j] == 'S':
            start = [j, i]
            currLoc[0] = [j, i, j, i, -1]
            currLoc[1] = [j, i, j, i, -1]
            break
    if start != [-1, -1]:
        break

setCurrLocNum = 0
#checkLeft
if start[0]!= 0 and content[start[1]][start[0]-1] in possibleLeft:
    currLoc[setCurrLocNum][0] -=1
    currLoc[setCurrLocNum][4] = content[start[1]][start[0]]
    setCurrLocNum += 1

#Check Right
if start[0] != len(content[start[1]])-1 and content[start[1]][start[0]+1] in possibleRight:
    currLoc[setCurrLocNum][0] +=1
    currLoc[setCurrLocNum][4] = content[start[1]][start[0]]
    setCurrLocNum += 1

#Check Down
if setCurrLocNum < 2 and start[1] != len(content)-1 and content[start[1]+1][start[0]] in possibleDown:
    currLoc[setCurrLocNum][1] +=1
    currLoc[setCurrLocNum][4] = content[start[1]][start[0]]
    setCurrLocNum += 1

#Check Up
if setCurrLocNum < 2 and start[1] != 0 and content[start[1]-1][start[0]] in possibleUp:
    currLoc[setCurrLocNum][1] -=1
    currLoc[setCurrLocNum][4] = content[start[1]][start[0]]
    setCurrLocNum += 1




while stepMap[currLoc[0][1]][currLoc[0][0]] == 0:
    stepNum +=1
    
    for i in range(len(currLoc)):
        currLoc[i][4] = content[currLoc[i][1]][currLoc[i][0]]
        stepMap[currLoc[i][1]][currLoc[i][0]] = stepNum

        if currLoc[i][4] == 'F':
            if not isPrevLoc(currLoc[i][0], currLoc[i][1]+1, currLoc[i][2], currLoc[i][3]):
                setPrevLoc(i)
                currLoc[i][1] +=1
            else:
                setPrevLoc(i)
                currLoc[i][0] +=1
            
        elif currLoc[i][4] == 'J':
            if not isPrevLoc(currLoc[i][0], currLoc[i][1]-1, currLoc[i][2], currLoc[i][3]):
                setPrevLoc(i)
                currLoc[i][1] -=1
            else:
                setPrevLoc(i)
                currLoc[i][0] -=1

        elif currLoc[i][4] == 'L':
            if not isPrevLoc(currLoc[i][0], currLoc[i][1]-1, currLoc[i][2], currLoc[i][3]):
                setPrevLoc(i)
                currLoc[i][1] -=1

            else:
                setPrevLoc(i)
                currLoc[i][0] +=1

        elif currLoc[i][4] == '7':
            if not isPrevLoc(currLoc[i][0], currLoc[i][1]+1, currLoc[i][2], currLoc[i][3]):
                setPrevLoc(i)
                currLoc[i][1] +=1

            else:
                setPrevLoc(i)
                currLoc[i][0] -=1

        elif currLoc[i][4] == '-':
            if not isPrevLoc(currLoc[i][0]+1, currLoc[i][1], currLoc[i][2], currLoc[i][3]):
                setPrevLoc(i)
                currLoc[i][0] +=1

            else:
                setPrevLoc(i)
                currLoc[i][0] -=1

        elif currLoc[i][4] == '|':
            if not isPrevLoc(currLoc[i][0], currLoc[i][1]+1, currLoc[i][2], currLoc[i][3]):
                setPrevLoc(i)
                currLoc[i][1] +=1

            else:
                setPrevLoc(i)
                currLoc[i][1] -=1


for i in range(len(content)):
    for j in range(len(content[i])):
        if stepMap[i][j] == 0: 
            content[i][j] = 0

NumEnclosed = 0

for i in range(len(stepMap)):
    inside = False
    isF = False
    isL = False
    for j in range(len(stepMap[i])):
        if not type(content[i][j]) == int:
            if content[i][j] == '|':
                inside = not inside
            
            elif content[i][j] == 'F':
                isF = True
            
            elif content[i][j] == 'L':
                isL = True

            elif content[i][j] == 'J':
                if isF:
                    isF = False
                    inside = not inside
                if isL:
                    isL = False

            elif content[i][j] == '7':
                if isF:
                    isF = False
                if isL:
                    inside = not inside
                    isL = False
        else:
            if inside:
                content[i][j] +=1
        

for j in range(len(stepMap[0])):
    inside = False
    isF = False
    is7 = False
    for i in range(len(stepMap)):
        if not type(content[i][j]) == int:
            if content[i][j] == '-':
                inside = not inside
            
            elif content[i][j] == 'F':
                isF = True
            
            elif content[i][j] == '7':
                is7 = True

            elif content[i][j] == 'J':
                if isF:
                    isF = False
                    inside = not inside
                if is7:
                    is7 = False

            elif content[i][j] == 'L':
                if isF:
                    isF = False
                if is7:
                    inside = not inside
                    is7 = False
        else:
            if inside:
                content[i][j] +=2
            
for i in content:
    for j in i:
        if j==3: NumEnclosed +=1

print(NumEnclosed)
