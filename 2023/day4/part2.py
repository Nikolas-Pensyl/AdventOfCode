# open the sample file used 
file = open('text.txt') 
  
# read the content of the file opened 
content = file.readlines() 

total = 0

cardWins = [0 for j in range(len(content))]
cards = [0 for j in range(len(content))]


for j in range(len(content)):
    content[j] = content[j].strip()
    
for j in range(len(content)-1, -1, -1):
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
            cardWins[j] +=1
            
        i +=1
        
for i in range(len(cards)):
    if i ==0:
        cards[i] = 1
    else:
        cards[i] = 1
        j = 0
        while j<i:
            if cardWins[j]+j-i>=0:
                cards[i] += cards[j]
            j+=1 
    total += cards[i]
                
print(total)
