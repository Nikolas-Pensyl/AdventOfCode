# open the sample file used 
file = open('text.txt') 
  
# read the content of the file opened 
content = file.readlines() 

total = 0

for l in content:
    firstNum = -1
    lastNum = -1
    for c in l:
        if c.isdigit(): 
            if firstNum == -1: 
                firstNum = int(c)
            
            lastNum = int(c)
    
    total += firstNum*10 + lastNum
        
print(total)
