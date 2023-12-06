# open the sample file used 
file = open('text.txt') 
  
# read the content of the file opened 
content = file.readlines() 

total = 0
for l in content:
    dims = [int(x) for x in l.strip().split("x")]
    largest = -1
    vol = 1
    sides = 0
    for i in range(len(dims)):
        vol *= dims[i]
        sides += 2*dims[i]
        if largest == -1 or largest<dims[i]:
            largest = dims[i]
    sides -= 2*largest
    total += sides+vol

print(total)
