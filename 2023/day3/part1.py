# open the sample file used 
file = open('text.txt') 
  
# read the content of the file opened 
content = file.readlines() 

total = 0

for j in range(len(content)):
    content[j] = content[j].strip()
  
for j in range(len(content)):
    l = content[j]
    i=0
    while i < len(l):
        if not l[i].isdigit():
            i +=1
            continue
    
        start= i
        while l[i].isdigit():
            i +=1
            if i == len(l):
                break
        end = i
        
        Num = int(l[start:end])
        
        isAdj = False
        
        if j!=0:
            if start!=0:
                if not content[j-1][start-1].isdigit() and content[j-1][start-1] != '.':
                    isAdj = True
            for k in range(start, end):
                if not content[j-1][k].isdigit() and content[j-1][k] != '.':
                    isAdj = True
            if end!=len(l):
                if not content[j-1][end].isdigit() and content[j-1][end] != '.':
                    isAdj = True
                        
        if j+1!=len(content):
            if start!=0:
                if not content[j+1][start-1].isdigit() and content[j+1][start-1] != '.':
                    isAdj = True
            for k in range(start, end+1):
                if not content[j+1][k].isdigit() and content[j+1][k] != '.':
                    isAdj = True
            if end!=len(l):
                if not content[j+1][end].isdigit() and content[j+1][end] != '.':
                    isAdj = True
        
        if end!=len(l):
            if not content[j][end].isdigit() and content[j][end] != '.':
                isAdj = True
        if start!=0:
            if not content[j][start-1].isdigit() and content[j][start-1] != '.':
                isAdj = True
        
        if(isAdj):
            total += Num

        i +=1
    
    
print(total)
