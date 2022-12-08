grid = []
ansGrid = []
gridLen = 0

with open("in.txt") as f:
    for row in f:
        lRow = list(row.strip())
        lRow = [int(x) for x in lRow]
        grid.append(lRow)
    gridLen = len(grid)

    def score(x ,y):
        # Search top
        topCount = 1
        i = x-1
        while i >= 0 and grid[x][y] > grid[i][y]:            
            i -= 1
            topCount += 1 if i >= 0 else 0

        # Search bottom
        bottomCount = 1
        i = x+1
        while i < gridLen and grid[x][y] > grid[i][y]:
            i += 1 
            bottomCount += 1 if i != gridLen else 0
        
        # Search left
        leftCount = 1
        i = y-1
        while i >= 0 and grid[x][y] > grid[x][i]:
            i -= 1
            leftCount += 1 if i >= 0 else 0            

        # Search right
        rightCount = 1
        i = y+1
        while i < gridLen and grid[x][y] > grid[x][i]:
            i += 1
            rightCount += 1 if i != gridLen else 0            
        return leftCount*rightCount*topCount*bottomCount
    
    maxScore = 0
    for i in range(1, gridLen-1):
        for j in range(1, gridLen-1):
            maxScore = max(maxScore, score(i, j))
    print(maxScore)


