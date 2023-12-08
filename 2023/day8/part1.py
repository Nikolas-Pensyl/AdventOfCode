
text = open("text.txt")
content = text.readlines()


instructions = content[0].strip()
maps = {}
lefrig = {"L": 0, "R": 1}
for i in range(2, len(content)):
    curr, eq,  left, right = content[i].split()
    right = right[0:len(right)-1]
    left = left[1:len(left)-1]
    
    maps[curr] = [left, right]

instruct_Index = 0
count = 0
currLoc = 'AAA'

while currLoc!='ZZZ':
    currLoc = maps[currLoc][lefrig[instructions[instruct_Index]]]
    
    count +=1
    instruct_Index +=1
    if instruct_Index == len(instructions):
        instruct_Index = 0
    
print(count)
