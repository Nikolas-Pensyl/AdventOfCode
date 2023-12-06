# open the sample file used 
file = open('text.txt') 
  
# read the content of the file opened 
content = file.readlines() 

total = 0

Loc = [0, 0]
Locs = {}

total +=1
Locs[str(Loc)] = 0

for c in content[0]:
    if c == "^":
        Loc[1] +=1
    elif c =="<":
        Loc[0] -=1
    elif c == ">":
        Loc[0] +=1
    elif c == "v":
        Loc[1] -=1
    
    index = Locs.get(str(Loc), -1)
    if  index == -1:
        total +=1
        Locs[str(Loc)] = 0
    else: 
        Locs[str(Loc)] = index +1

print(total)
