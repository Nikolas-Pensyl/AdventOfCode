# open the sample file used 
file = open('text.txt') 
  
# read the content of the file opened 
content = file.readlines()

bad = ["ab", "cd", "pq", "xy"]
vowels = "aeiou"
total = 0
for l in content:
    vowelC = 0
    isBad = False
    for b in bad:
        if l.find(b) !=-1:
            isBad = True
            break
    if isBad:
        continue

    good1 = False

    for i in range(len(l)):
        if i !=0 and l[i] == l[i-1]:
            good1 = True
        
        if l[i] in vowels:
            vowelC +=1

    if good1 and vowelC>=3:
        total +=1

print(total)
