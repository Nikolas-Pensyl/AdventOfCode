# open the sample file used 
file = open('text.txt') 
  
# read the content of the file opened 
content = file.readlines() 

total = 0

for j in range(len(content)):
    content[j] = content[j].strip()
    
for j in range(len(content)):
    cardNum = j+1
    l = content[j]
    i=l.find(":")+1
    
    isWinningNums = True
    winningNums = []
    score = 0
    while i<len(l):
        if i!=len(l) and not l[i].isdigit():
            if(l[i]=='|'):
                isWinningNums = False
            i +=1
            continue
        
        startNum = i
        while i!=len(l) and l[i].isdigit():
            i+=1
        
        num = int(l[startNum:i])
        if isWinningNums:
            winningNums.append(num)
        elif num in winningNums:
            if score == 0:
                score = 1
            else:
                score *=2
            
        i +=1
    
    total += score
        
print(total)
