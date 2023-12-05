# open the sample file used 
file = open('text.txt') 
  
# read the content of the file opened 
content = file.readlines() 

floor = 0
count = 0
for l in content:
    for c in l:
        count +=1
        if c == "(":
            floor +=1
        else:
            floor -=1
        
        if floor ==-1:
            print(count)
            break
