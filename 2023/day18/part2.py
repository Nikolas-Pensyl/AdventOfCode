import ast

#0 = Right, 1 = Down, 2 = Left, 3 = Up
lrud = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}

content = [[lrud[int(line.split()[2][-2])], ast.literal_eval('0x'+line.split()[2][2:-2])] for line in open("text.txt").read().strip().splitlines()]

field = [[1]]
cols = [1]
rows = [1]
x = 0
y = 0

#Lazy, but probably could have combined addRow and addCol if I wanted just had to transpose the field before sending it into just one of the functions

def addRow(newRow, x, y, dy):
    if y +dy == -1 or y+dy == len(rows):
        if y+dy == -1:
            rows.insert(0, newRow-1)
            rows.insert(0, 1)
            field.insert(0, [0 for i in range(len(field[y]))])
            field.insert(0, [0 for i in range(len(field[y]))])
            field[0][x] = 1
            field[1][x] = 1
        else:
            rows.append(newRow-1)
            rows.append(1)
            field.append([0 for i in range(len(field[y]))])
            field.append([0 for i in range(len(field[y]))])
            field[y+1][x] = 1
            field[y+2][x] = 1
            y += 2
        return y

    y += dy
    field[y][x] = 1
    if newRow>rows[y]:
        return addRow(newRow-rows[y], x, y, dy)
    elif newRow== rows[y]:
        return y

    rows.insert(y if dy == -1 else y+1, rows[y]- newRow)
    rows.insert(y+1, 1)
    field.insert(y if dy==-1 else y+1, [0 for j in range(len(field[y]))])
    field.insert(y+1, [0 for j in range(len(field[y]))])
    rows[y+2 if dy == -1 else y] = newRow-1
    y = y+1
    field[y][x] = 1
    if dy == -1:
        for ix in range(len(field[y if dy == -1 else y+1])):
            if cols[ix] == 1 and field[y-2][ix] == 1 and field[y+1][ix] == 1 and ix != x:
                field[y][ix] = 1
                field[y-1][ix] = 1
    else:
        for ix in range(len(field[y if dy == -1 else y+1])):
            if cols[ix] == 1 and field[y-1][ix] == 1 and field[y+2][ix] == 1 and ix != x:
                field[y][ix] = 1
                field[y+1][ix] = 1

    return y


def addCol(newCol, x, y, dx):
    if x +dx == -1 or x+dx == len(cols):
        if x+dx == -1:
            cols.insert(0, newCol-1)
            cols.insert(0, 1)
            for y, line in enumerate(field):
                line.insert(0, 0)
                line.insert(0, 0)
            field[y][1] = 1
            field[y][0] = 1
        else:
            cols.append(newCol-1)
            cols.append(1)
            for line in field:
                line.append(0)
                line.append(0)
            field[y][x+1] = 1
            field[y][x+2] = 1
            x += 2
        return x

    x += dx
    field[y][x] = 1
    if newCol>cols[x]:
        return addCol(newCol-cols[x], x, y, dx)
    elif newCol== cols[x]:
        return x

    cols.insert(x if dx == -1 else x+1, cols[x]- newCol)
    cols.insert(x+1, 1)
    for line in field:
        line.insert(x if dx==-1 else x+1, 0)
        line.insert(x+1, 0)

    cols[x+2 if dx == -1 else x] = newCol-1
    x = x+1
    field[y][x] = 1
    if dx == -1:
        for iy in range(len(field)):
            if rows[iy] == 1 and field[iy][x-2] == 1 and field[iy][x+1] == 1 and iy !=y:
                field[iy][x-1] = 1
                field[iy][x] = 1
    else:
        for iy in range(len(field)):
            if rows[iy] == 1 and field[iy][x-1] == 1 and field[iy][x+2] == 1 and iy !=y:
                field[iy][x+1] = 1
                field[iy][x] = 1
    
    return x


#Go Around
for k, move in enumerate(content):
    if move[0][0] != 0:
        x = addCol(move[1], x, y, move[0][0])
    else:
        y = addRow(move[1], x, y, move[0][1])
      

Up = False
inside = False
#Add Area
for i, line in enumerate(field):
    j = 0
    while j<len(line):
        if j != len(line)-1 and line[j+1] >0 and line[j] >0:
            if i!= 0 and field[i-1][j] >0 :
                Up = True
            while j != len(line)-1 and line[j+1] >0:
                j += 1
        
            if (i!= 0 and field[i-1][j] > 0 and not Up) or (Up and i!= len(field)-1 and field[i+1][j] >0):
                    inside = not inside
            Up = False
        elif line[j] >0:
            inside = not inside
        
        elif inside:
            line[j] -= 1
    
        j +=1


#Get Sum
print(sum([sum([rows[y] * cols[x] * abs(num) for x, num in enumerate(line)]) for y, line in enumerate(field)]))
