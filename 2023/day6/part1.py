# open the sample file used 
file = open('text.txt') 
  
# read the content of the file opened 
content = file.readlines()

index = content[0].find(":")+1
times = [int(x) for x in content[0][index:len(content[0])].strip().split()]

index = content[1].find(":")+1
dists = [int(x) for x in content[1][index:len(content[1])].strip().split()]

total = 1

for i in range(len(times)):
    beaten = 0
    for j in range(1, times[i]):
        if j*(times[i]-j) > dist[i]:
            beaten +=1
    total *= beaten
    
print(total)
