# open the sample file used 
file = open('text.txt') 
  
# read the content of the file opened 
content = file.readlines() 

total = 0

Loc = [[0, 0], [0, 0]]
Locs = {}

total +=1
Locs[str(Loc[0])] = 0


count = 0
for c in content[0]:
    if c == "^":
        Loc[count%2][1] +=1
    elif c =="<":
        Loc[count%2][0] -=1
    elif c == ">":
        Loc[count%2][0] +=1
    elif c == "v":
        Loc[count%2][1] -=1
    
    index = Locs.get(str(Loc[count%2]), -1)
    if  index == -1:
        total +=1
        Locs[str(Loc[count%2])] = 0
    else: 
        Locs[str(Loc[count%2])] = index +1
    
    count +=1

print(total)
