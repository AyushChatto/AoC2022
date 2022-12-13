grid = []

with open("in.txt") as f:
    for row in f:
        grid.append(list(row.strip()))

# Now just run a fucking BFS
from collections import deque

queue = deque([])
goal = ()
visited = set()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            queue.append((i, j, 0))
            grid[i][j] = 'a'
        elif grid[i][j] == 'E':
            goal = (i, j)
            grid[i][j] = 'z'

def isDiffLessThan2(a, b):
    return ord(a) - ord(b) < 2

while len(queue) > 0:
    i, j, step = queue.popleft()
    cell = (i, j)

    if cell == goal:
        print(step)
        break

    else:
        if i > 0 and (i - 1, j) not in visited and isDiffLessThan2(grid[i - 1][j], grid[i][j]):
            queue.append((i - 1, j, step + 1))
            visited.add((i - 1, j))
        
        if j > 0 and (i, j - 1) not in visited and isDiffLessThan2(grid[i][j - 1], grid[i][j]):
            queue.append((i, j - 1, step + 1))
            visited.add((i, j - 1))

        if i < len(grid) - 1 and (i + 1, j) not in visited and isDiffLessThan2(grid[i + 1][j], grid[i][j]):
            queue.append((i + 1, j, step + 1))
            visited.add((i + 1, j))

        if j < len(grid[0]) - 1 and (i, j + 1) not in visited and isDiffLessThan2(grid[i][j + 1], grid[i][j]):
            queue.append((i, j + 1, step + 1))
            visited.add((i, j + 1))
        

    



