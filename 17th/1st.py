
jets = ""
pieces = [
    # Flatline
    [(i, 0) for i in range(2,6)],
    # Plus
    [(3, 0), (2, 1), (3, 1), (4, 1), (3, 2)],
    # L-shape
    [(2, 0), (3, 0), (4, 0), (4, 1), (4, 2)],
    # I-shape
    [(2, i) for i in range(4)],
    # Box
    [(2, 0), (3, 0), (2, 1), (3, 1)]
]

with open('test.txt') as f:
    for row in f:
        jets = row

ji = 0
height = 0
occupied = set()

def shiftLeft(piece):
    ans = []
    for i in piece:
        if (i[0] - 1, i[1]) in occupied or i[0] == 0:
            return piece
        ans.append((i[0] - 1, i[1]))
    return ans

def shiftRight(piece):
    ans = []
    for i in piece:
        if (i[0] + 1, i[1]) in occupied or i[0] == 6:
            return piece
        ans.append((i[0] + 1, i[1]))
    return ans

def shiftDown(piece):
    ans = []
    for i in piece:
        if (i[0], i[1] - 1) in occupied or i[1] == 0:
            return piece
        ans.append((i[0], i[1] - 1))
    return ans

def cleanup():
    global occupied
    newSet = set()
    for j in occupied:
        if height - j[1] <= 50:
            newSet.add(j)
    occupied = newSet

for i in range(2022):
    cleanup()
    piece = pieces[i % 5][:]
    piece = [(x[0], x[1] + height + 3) for x in piece]

    while True:
        if jets[ji] == '<':
            piece = shiftLeft(piece)
        else:            
            piece = shiftRight(piece)
        
        ji += 1
        ji %= len(jets)

        newP = shiftDown(piece)
        if newP == piece:
            occupied.update(newP)
            height = max(height, max([i[1] for i in newP]) + 1)
            break
        else:
            piece = newP

print(height)
        
            

    

    

    







