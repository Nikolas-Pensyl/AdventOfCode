content = open("text.txt").read().splitlines()
startPos = ()
for y, line in enumerate(content):
    for x, char in enumerate(line):
        if char == 'S':
            startPos = (x, y)

moves = [(startPos[0], startPos[1], 0)]
seen = {(startPos[0], startPos[1])}
completed = {(startPos[0], startPos[1])}

while moves:
    x, y, n = moves.pop(0)
    n += 1
    for xs, ys in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx = x+xs
        ny = y+ys
        if -1<nx<len(content[0]) and -1<ny<len(content) and content[ny][nx] != '#' and (nx, ny) not in seen:
            seen.add((nx, ny))
            if n %2 == 0:
                completed.add((nx, ny))
            if n!=64 and (nx, ny, n) not in moves:
                moves.append((nx, ny, n))
                

print(len(completed))
