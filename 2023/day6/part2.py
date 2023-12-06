# open the sample file used 
file = open('text.txt') 
  
# read the content of the file opened 
content = file.readlines()

index = content[0].find(":")+1
times = [int(x) for x in content[0][index:len(content[0])].strip().split()]
time = 0
timeStr = ''

index = content[1].find(":")+1
dists = [int(x) for x in content[1][index:len(content[1])].strip().split()]
dist = 0
distStr = ''

for i in range(len(times)):
    timeStr += str(times[i])
    distStr += str(dists[i])
time = int(timeStr)
dist = int(distStr)

firstWin = -1
i=1
while i<time:
    if firstWin==-1:
        if (i*(time-i)>dist):
            firstWin = i
            break
    i +=1
    
total = time-firstWin*2+1

print(total)
