# open the sample file used 
file = open('text.txt') 
  
# read the content of the file opened 
content = file.readlines() 

total = 0

clrs = ['red', 'green', 'blue']
gameId = 1
for l in content:
    index = l.find(":")+1
    
    maxBlue = 0
    maxGreen =0
    maxRed = 0

    while index < len(l):
        if not l[index].isdigit():
            index +=1
            continue
        
        start = index
        while l[index].isdigit():
            index +=1
            
        Num = int(l[start:index])
        
        smallestIn = len(l)
        selectClr = ''
        
        for clr in clrs:
            clrIn = l.find(clr, index)
            if clrIn != -1 and clrIn < smallestIn:
               smallestIn = clrIn
               selectClr = clr
    
        if selectClr == 'red' and Num>maxRed:
            maxRed = Num
        
        if selectClr == 'blue' and Num>maxBlue:
            maxBlue = Num
        
        if selectClr == 'green' and Num>maxGreen:
            maxGreen = Num
        
    total += maxGreen*maxBlue*maxRed
    
    gameId +=1

print(total)
