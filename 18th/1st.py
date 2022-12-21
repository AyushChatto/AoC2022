squares = set()
with open("in.txt") as f:
    for row in f:
        row = row.strip().split(',')
        row = [int(x) for x in row]
        squares.add(tuple(row))

faceCount = 0
for i in squares:
    for dir in [0, 1, 2]:
        for offset in [-1, 1]:
            newSq = list(i[:])
            newSq[dir] += offset
            if tuple(newSq) not in squares:
                faceCount += 1
print(faceCount)
            


