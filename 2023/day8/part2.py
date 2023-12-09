
text = open("text.txt")
content = text.readlines()


instructions = content[0].strip()
maps = {}
loops = []
lefrig = {"L": 0, "R": 1}
currLocs = []
InnerLoop = []

#Get All the mappings and starting Locations
for i in range(2, len(content)):
    curr, eq,  left, right = content[i].split()
    right = right[0:len(right)-1]
    left = left[1:len(left)-1]
    
    maps[curr] = [left, right]
    if curr[2] == 'A':
        currLocs.append(curr)
        loops.append({curr: 0})

instruct_Index = 0
count = 0

#Find where the loop starts at instruction 0 based on each starting location
for i in range(len(currLocs)):
    count = 0
    instruct_Index = 0
    while True:
        currLocs[i] = maps[currLocs[i]][lefrig[instructions[instruct_Index]]]          

        instruct_Index +=1
        count += 1

        if instruct_Index == len(instructions):
            instruct_Index = 0
            if loops[i].get(currLocs[i], -1) == -1:
                loops[i][currLocs[i]] = count
            else:
                InnerLoop.append([currLocs[i], count, loops[i].get(currLocs[i]), count-loops[i].get(currLocs[i])])
                break

print(InnerLoop, '\n')

#Get all ending locations based on each loop
for i in range(len(currLocs)):
    InnerLoop[i].append([])
    count = 0
    instruct_Index = 0
    while True:
        currLocs[i] = maps[currLocs[i]][lefrig[instructions[instruct_Index]]]
        instruct_Index +=1
        count +=1

        if currLocs[i][2] == 'Z':
            InnerLoop[i][4].append([currLocs[i], count%InnerLoop[i][3]])

        if instruct_Index == len(instructions):
            instruct_Index = 0
            if currLocs[i] == InnerLoop[i][0]:
                print(InnerLoop[i])
                break


#Get the count where all the endings lineup
#Probably could optimize this somehow
i = 0
allEqual = False
while not allEqual:
    allEqual = True
    i +=1
    for j in range(1, len(InnerLoop)):
        if (i*InnerLoop[0][3] + InnerLoop[0][4][0][1]) % InnerLoop[j][3] != InnerLoop[j][4][0][1]:
            allEqual = False
            break
    

#Print the how many times to loop the first loop
#Print the ending location(loop length * number of times to loop  +  ending location compared to loop start  +  starting count of the loop)
print(i, i*InnerLoop[0][3] + InnerLoop[0][4][0][1]+InnerLoop[0][2])
