import ast

lrud = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}

content = [[lrud[int(line.split()[2][-2])], ast.literal_eval('0x'+line.split()[2][2:-2])] for line in open("text.txt").read().strip().splitlines()]

x = 0
y = 0

Xmax = 0
Xmin = 0

Ymax = 0
Ymin = 0

for move in content:
    if move[0] == 'R':
        x += move[1]
    elif move[0] == 'L':
        x -= move[1]
    elif move[0] == 'U':
        y -= move[1]
    else:
        y += move[1]
    
    Xmax = max(x,Xmax)
    Xmin = min(x, Xmin)
    Ymax = max(y, Ymax)
    Ymin = min(y, Ymin)

width = (Xmax - Xmin)+1
height = (Ymax - Ymin)+1

field = [[0 for i in range(width)] for j in range(height)]
x = abs(Xmin)
y = abs(Ymin)

for move in content:
    if move[0] == 'R':
        for j in range(x, move[1]+x):
            field[y][j] = 1
        x += move[1]
    elif move[0] == 'L':
        for j in range(x, x-move[1], -1):
            field[y][j] = 1
        x -= move[1]
    elif move[0] == 'U':
        if y-move[1] <0:
            print(y, move[1])
        for j in range(y, y-move[1], -1):
            field[j][x] = 1
        y -= move[1]
    else:
        for j in range(y, y+move[1]):
            field[j][x] = 1
        y += move[1]
    
inside = False
Up = False

for i, line in enumerate(field):
    j = 0
    while j<len(line):
        if j != len(line)-1 and line[j+1] == 1 and line[j] == 1:
            if i!= 0 and field[i-1][j] == 1:
                Up = True
            while j != len(line)-1 and line[j+1] == 1:
                j += 1
        
            if (i!= 0 and field[i-1][j] == 1 and not Up) or (Up and i!= len(field)-1 and field[i+1][j] == 1):
                    inside = not inside
            Up = False
        elif line[j] == 1:
            inside = not inside
        
        elif inside:
            line[j] += 2
    
        j +=1
            

print(sum([sum([1 if char >0 else 0 for char in line]) for line in field]))
