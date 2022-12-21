from collections import deque

squares = set()
maxes = [0, 0, 0]
mins = [20, 20, 20]

with open("in.txt") as f:
    for row in f:
        row = row.strip().split(',')
        row = [int(x) for x in row]
        squares.add(tuple(row))
        maxes = [max(maxes[i], x) for i, x in enumerate(row)]
        mins = [min(mins[i], x) for i, x in enumerate(row)]

start = [x + 1 for x in maxes]
end = [x - 1 for x in mins]
faceCount = 0
queue = deque([start])
visited = set()

def neighbours(node):
    ans = []
    for dir in range(len(node)):
        for offset in [-1, 1]:
            newSq = node[:]
            newSq[dir] += offset
            if newSq[dir] <= start[dir] and newSq[dir] >= end[dir]:
                ans.append(newSq)
    return ans

while len(queue) > 0:
    node = queue.popleft()
    adj = neighbours(node)
    
    for i in adj:
        ti = tuple(i)
        if ti in squares:
            faceCount += 1

        elif ti not in visited:
            visited.add(ti)
            queue.append(i)

print(faceCount)
    



            


