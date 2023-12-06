# open the sample file used 
file = open('text.txt') 
  
# read the content of the file opened 
content = file.readlines()

total = 0

for l in content:
    good1 = False
    good2 = False

    for i in range(len(l)):
        if i >1 and l[i] == l[i-2]:
            good1 = True
        
        if i != 0 and l[i+1:len(l)].find(l[i-1:i+1]) != -1:
            good2 = True
            
        if good1 and good2:
            break

    if good1 and good2:
        total +=1

print(total)
