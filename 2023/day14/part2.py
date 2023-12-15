from copy import deepcopy
file = open("text.txt")
content = [[char for char in line] for line in file.read().strip().splitlines()]

#Not that great tried to reverse the string rather than make a reverse for loop method
#Hate 'lists' not hashable have to get more familiar with map function and tuples


#move
#Default = North
prevStates = {}
def newMove(state):
    prevState = str(state)
    newState = prevStates.get(str(state), -1)
    if newState != -1:
        return newState

    moveTo = -1
    zeroCount = 0

    for j in range(len(state)):
        if state[j] == '.' and moveTo == -1:
            moveTo = j
        
        if state[j] == 'O' and moveTo != -1:
            zeroCount += 1
        
        if state[j]== '#' and moveTo != -1:
            for k in range(moveTo, j):
                if zeroCount>0:
                    zeroCount -=1
                    state[k] = 'O'
                else:
                    state[k] = '.'
            
            moveTo = -1
        
    if moveTo != -1:
        for k in range(moveTo, len(state)):
            if zeroCount>0:
                zeroCount -=1
                state[k] = 'O'
            else:
                state[k] = '.'
    
    prevStates[prevState] = state
    return state

prevStatesSE = {}
def newMoveSE(state):
    prevState = str(state)
    newState = prevStatesSE.get(str(state), -1)
    if newState != -1:
        return newState

    moveTo = -1
    zeroCount = 0

    for j in range(len(state)-1, -1, -1):
        if state[j] == '.' and moveTo == -1:
            moveTo = j
        
        if state[j] == 'O' and moveTo != -1:
            zeroCount += 1
        
        if state[j]== '#' and moveTo != -1:
            for k in range(moveTo, j, -1):
                if zeroCount>0:
                    zeroCount -=1
                    state[k] = 'O'
                else:
                    state[k] = '.'
            
            moveTo = -1
        
    if moveTo != -1:
        for k in range(moveTo, -1, -1):
            if zeroCount>0:
                zeroCount -=1
                state[k] = 'O'
            else:
                state[k] = '.'
    
    prevStatesSE[prevState] = state
    return state


def getTotal(full):
    total = 0
    for i in range(len(full[0])):
        for j in range(len(full)):
            if full[j][i] == 'O':
                total += len(full)-j
    return total

modNum = 0
seen = {str(content): content}
seenList = [str(content)]
count = 0
for x in range(4000000000):
    content = [list(a) for a in list(zip(*content))]

    for i in range(len(content)):
        if modNum == 2 or modNum == 3:
            content[i] = newMoveSE(content[i])
        else:
            content[i] = newMove(content[i])

    modNum = (modNum+1)%4
    if modNum == 0:
        count += 1
        if str(content) not in seen:
            seen[str(content)] = content
            seenList.append(str(content))
        else:
            first = seenList.index(str(content))
            index  = ((1000000000 - first) % (count - first)) + first
            print(getTotal(seen[seenList[index]]))
            break



