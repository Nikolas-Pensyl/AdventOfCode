# open the sample file used 
file = open('text.txt') 
  
# read the content of the file opened 
content = file.readlines()

lights = [[0 for j in range(1000)] for k in range(1000)]

instructions = ["on", "off", "togg"]

for l in content:
    instruct = ''
    for k in instructions:
        if l.find(k) != -1:
            instruct = k
    bounds = [int(y) for x in l.split() for y in x.split(",") if x[0][0].isdigit()]

    for x in range(bounds[0], bounds[2]+1):
        for y in range(bounds[1], bounds[3]+1):
            if instruct == "on":
                lights[x][y] += 1
            elif instruct == "off" and lights[x][y]>0:
                lights[x][y] -= 1
            elif instruct == "togg": 
                lights[x][y] += 2

total = 0
for i in lights:
    for j in i:
            total += j

print(total)
