charList = [[ord(char) for char in line] for line in open("text.txt").read().strip().split(',')]

total = 0
for i in charList:
    currValue = 0
    for j in i:
        currValue = ((currValue+j)*17)%256
    total += currValue

print(total)
