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
        NumOfNums = 0
        Gears = []
        if l[i].isdigit() or l[i]=='.':
            i +=1
            continue
        
        #Left
        if i!=0 and l[i-1].isdigit():
            startLeft = i-1
            NumOfNums += 1
            while startLeft!=-1 and l[startLeft].isdigit():
                startLeft -=1
            startLeft +=1
            Gears.append(int(l[startLeft:i]))
            
        #Right
        if i!=len(l) and l[i+1].isdigit():
            startRight = i+1
            NumOfNums += 1
            while startRight!=len(l) and l[startRight].isdigit():
                startRight +=1
            Gears.append(int(l[i+1:startRight]))
            
        #Top
        if j!=0:
            start = i
            if i!=0:
                start -=1
                while start-1!=-1 and content[j-1][start].isdigit():
                    start -=1
            curr = start
            while curr <=i+1 and curr < len(content[j-1]):
                if not content[j-1][curr].isdigit():
                    curr +=1
                    continue
                startNum = curr
                
                NumOfNums += 1
                while curr <len(content[j-1]) and content[j-1][curr].isdigit():
                    curr +=1
                
                Gears.append(int(content[j-1][startNum:curr]))
                curr +=1
                
        #Bottom
        if j!=len(content):
            start = i
            if i!=0:
                start -=1
                while start-1!=-1 and content[j+1][start].isdigit():
                    start -=1
            curr = start
            while curr <=i+1 and curr < len(content[j+1]):
                if not content[j+1][curr].isdigit():
                    curr +=1
                    continue
                startNum = curr
                
                NumOfNums += 1
                while curr <len(content[j+1]) and content[j+1][curr].isdigit():
                    curr +=1
                if j==15: print(i, startNum, curr)
                Gears.append(int(content[j+1][startNum:curr]))
                curr +=1
        
        if NumOfNums == 2:
            total += Gears[0]*Gears[1]
        
        i +=1
    
    
print(total)
