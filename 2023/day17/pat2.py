from heapq import heappop, heappush

file = open("text.txt").read().strip()
content = [list(map(int, line)) for line in file.splitlines()]

maxX = len(content[0])-1
maxY = len(content)-1
    
moves = []
seen = set()

#total, x, y, dx, dy, forward
moves.append((0, 0, 0, 0, 0, 0))

while moves:
    total, x, y, dx, dy, forward = heappop(moves)

    if (x, y, dx, dy, forward) in seen:
        continue


    seen.add((x, y, dx, dy, forward))
    if x==maxX and y==maxY:
        print(total)
        break

    if forward<10 and -1<x+dx<=maxX and -1<y+dy<=maxY and (dx, dy)!= (0, 0): 
        heappush(moves, (total+content[y+dy][x+dx], x+dx, y+dy, dx, dy, forward+1))

    if forward == 0 or forward>3:
        for idx, idy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if -1<x+idx<=maxX and -1<y+idy<=maxY and (idx, idy) != (dx, dy) and (-idx, -idy) != (dx, dy):
                heappush(moves, (total+content[y+idy][x+idx], x+idx, y+idy, idx, idy, 1))
