grid = []
ansGrid = []
gridLen = 0

with open("in.txt") as f:
    for row in f:
        lRow = list(row.strip())
        lRow = [int(x) for x in lRow]
        grid.append(lRow)
    gridLen = len(grid)
    ansGrid = [[False] * gridLen for _ in range(gridLen)]

    # Top sweep
    maxArr = [-1] * gridLen
    for j, arr in enumerate(grid):
        for i, v in enumerate(arr):
            if v > maxArr[i]:
                maxArr[i] = v
                ansGrid[j][i] = True
    
    # Bottom sweep
    maxArr = [-1] * gridLen
    for j, arr in enumerate(grid[::-1]):
        for i, v in enumerate(arr):
            if v > maxArr[i]:
                maxArr[i] = v
                ansGrid[-1-j][i] = True

    # Left Sweep
    maxArr = [-1] * gridLen
    for a in range(gridLen):
        arr = [grid[x][a] for x in range(gridLen)]
        for i, v in enumerate(arr):
            if v > maxArr[i]:
                maxArr[i] = v
                ansGrid[i][a] = True

    # Right Sweep
    maxArr = [-1] * gridLen
    for a in range(gridLen-1, -1, -1):
        arr = [grid[x][a] for x in range(gridLen)]
        for i, v in enumerate(arr):
            if v > maxArr[i]:
                maxArr[i] = v
                ansGrid[i][a] = True

    counter = 0
    for i in ansGrid:
        for j in i:
            counter += 1 if j else 0
    print(counter)



    
