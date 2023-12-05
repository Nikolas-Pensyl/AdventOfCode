# open the sample file used 
file = open('text.txt') 
  
# read the content of the file opened 
content = file.readlines() 

NumArr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

total = 0

for l in content:
    firstNum = -1
    lastNum = -1
    
    firstIndex = -1
    lastIndex = -1
    for num in range(len(NumArr)):
        index = l.find(NumArr[num])
        while index != -1:
            
            if index<firstIndex or firstIndex == -1:
                firstIndex = index
                firstNum = num%10

            if index>lastIndex:
                lastIndex = index
                lastNum = num%10
            
            index = l.find(NumArr[num], index+1)
            
    total += firstNum*10 + lastNum

print(total)
