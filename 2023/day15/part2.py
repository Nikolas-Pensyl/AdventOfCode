#Should have looked at the input text initially assumed that the labels were two characters
def getBox(line):
    currValue = 0
    index  = 0
    for i, j in enumerate(line):
        if j== '-' or j =='=':
            index = i
            break
        currValue = ((currValue+ord(j))*17)%256
    
    if '=' in line:
        return [line[0:index], currValue, int(line[-1])]
    
    return [line[0:index], currValue]

lines = [getBox(line) for line in open("text.txt").read().strip().split(',')]

boxes = [[] for i in range(256)]

lensSet = {}
for line in lines:
    if len(line)==3:
        if line[0] not in lensSet:
            boxes[line[1]].append(line[0])
        
        lensSet[line[0]] = line[2]
    else:
        if line[0] in lensSet:
            lensSet.pop(line[0])
            boxes[line[1]].pop(boxes[line[1]].index(line[0]))

total = 0
for boxNum, box in enumerate(boxes):
    for boxIndex, label in enumerate(box):
        total += (boxNum+1) * (boxIndex+1) * (lensSet[label])

print(total)
