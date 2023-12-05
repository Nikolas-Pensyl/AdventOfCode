# open the sample file used 
file = open('text.txt') 
  
# read the content of the file opened 
content = file.readlines() 

lowest_loc = -1

maps = [[], [], [], [], [], [], []]
seeds = []

index = content[0].find(":")+1
seedsRanges = [int(x) for x in content[0][index:len(content[0])].strip().split()]
currentArr = [[seedsRanges[k], seedsRanges[k+1]] for k in range(0, len(seedsRanges), 2)]



#Get Mapping
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

#Convert Seeds
for map in maps:
    i = 0
    while i < len(currentArr):
        curr = currentArr[i][0]
        currRange = currentArr[i][1]
        
        for innerMap in map:
            if curr>=innerMap[1] and curr+currRange<=innerMap[1]+innerMap[2]:
                curr = curr-innerMap[1]+innerMap[0]
                break
            elif curr>=innerMap[1] and curr+currRange>innerMap[1]+innerMap[2] and curr<innerMap[1]+innerMap[2]:
                currentArr.append([innerMap[1]+innerMap[2],  currRange+curr-innerMap[1]-innerMap[2]])
                
                currRange = innerMap[1]+innerMap[2]-curr
                curr = curr-innerMap[1]+innerMap[0]
                break
            elif curr<innerMap[1] and curr+currRange>innerMap[1] and curr+currRange<=innerMap[1]+innerMap[2]:
                currentArr.append([curr,  innerMap[1]-curr])
                
                currRange = curr+currRange-innerMap[1]
                curr = innerMap[0]
                break
            elif curr<innerMap[1] and curr+currRange>innerMap[1]+innerMap[2]:
                currentArr.append([curr, innerMap[1]-curr])
                currentArr.append([innerMap[1]+innerMap[2], curr+currRange-innerMap[1]-innerMap[2]])
                
                
                currRange = innerMap[2]
                curr = innerMap[0]
                break

        currentArr[i][0] = curr
        currentArr[i][1] = currRange
        
        i+=1


finalLocsMin = [d[0] for d in currentArr]

print(min(finalLocsMin))
