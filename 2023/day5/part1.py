# open the sample file used 
file = open('text.txt') 
  
# read the content of the file opened 
content = file.readlines() 

lowest_loc = -1

maps = [[], [], [], [], [], [], []]
seeds = []

index = content[0].find(":")+1
seeds = [int(x) for x in content[0][index:len(content[0])].strip().split()]
finalLocs = []

i = 3
mapIndex = 0
innerMapIndex = 0
while i<len(content):
    if content[i].find("map")!=-1:
        mapIndex +=1
        innerMapIndex = 0
        i +=1
        continue
    
    if len(content[i])<2:
       i +=1
       continue
   
    maps[mapIndex].append([int(x) for x in content[i].strip().split()])
    i+=1

for seed in seeds:
    curr = seed

    for map in maps:
        for innerMap in map:
            if curr>innerMap[1] and curr<innerMap[1]+innerMap[2]:
                curr = curr-innerMap[1]+innerMap[0]
                break
    
    finalLocs.append(curr)

print(min(finalLocs))
