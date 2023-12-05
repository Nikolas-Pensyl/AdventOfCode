# open the sample file used 
file = open('text.txt') 
  
# read the content of the file opened 
content = file.readlines() 

total = 0

for l in content:
    dims = [int(x) for x in l.strip().split("x")]
    smallest = -1
    for i in range(len(dims)):
        for j in range(i+1, len(dims)):
            area = dims[i]*dims[j]
            total += 2*area
            if smallest == -1 or area<smallest:
                smallest = area
    
    total += smallest

print(total)
