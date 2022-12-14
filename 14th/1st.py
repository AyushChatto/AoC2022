
grid = set()
# dgrid = set()

def addCoords(coords):
    for i in range(len(coords) - 1):
        (x1, y1), (x2, y2) = coords[i], coords[i + 1]
        
        if x1 == x2:
            while y1 < y2:
                grid.add((x1, y1))
                y1 += 1
                
            while y2 <= y1:
                grid.add((x1, y1))
                y1 -= 1

        else:
            while x1 < x2:
                grid.add((x1, y1))
                x1 += 1
                
            while x2 <= x1:
                grid.add((x1, y1))
                x1 -= 1

# ITERATE VERTICAL FIRST

with open("in.txt") as f:
    for row in f:
        row = row.split(' -> ')
        coords = [[int(y) for y in x.split(",")] for x in row]
        addCoords(coords)
    
    maxFloor = max([x[1] for x in grid])
    # If any sand were to proceed to a floor 1 greater than maxFloor, we have hit our sandcap
    sandCount = 0
    sandPos = (500, 0)
    while True:
        x, y = sandPos
        if y > maxFloor:
            print(sandCount)
            break

        if (x, y + 1) not in grid:
            sandPos = (x, y + 1)

        elif (x - 1, y + 1) not in grid:
            sandPos = (x - 1, y + 1)

        elif (x + 1, y + 1) not in grid:
            sandPos = (x + 1, y + 1)
        
        else:
            grid.add(sandPos)
            # dgrid.add(sandPos)
            sandCount += 1
            sandPos = (500, 0)

            # for i in range(0, 11):
            #     s = ""
            #     for j in range(492, 505):
            #         if (j , i) in grid and (j , i ) in dgrid:
            #             s += "o"
            #         elif (j, i) in grid:
            #             s += "#"
            #         else:
            #             s += "."
            #     print(s)
            # print()




        
