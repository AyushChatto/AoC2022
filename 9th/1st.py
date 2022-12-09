headLoc = [0, 0]
tailLoc = [0, 0]
visited = set([])

def moveTail(h, t):
    h0, h1 = h
    t0, t1 = t
    if abs(h0 - t0) <= 1 and abs(h1 - t1) <= 1:
        return
    elif h0 != t0 and h1 != t1:
        # Diagonal movement
        t[0] += 1 if h0 > t0 else 0
        t[0] -= 1 if h0 < t0 else 0
        t[1] += 1 if h1 > t1 else 0
        t[1] -= 1 if h1 < t1 else 0
    elif h0 != t0:
        # Horizontal movement
        t[0] += 1 if h0 > t0 else 0
        t[0] -= 1 if h0 < t0 else 0
    elif h1 != t1:
        # Vertical movement
        t[1] += 1 if h1 > t1 else 0
        t[1] -= 1 if h1 < t1 else 0
    



def makeMovements(h, t, d, s):
    for i in range(s):
        if d == 'U':
            h[1] += 1
        elif d == 'D':
            h[1] -= 1
        elif d == 'L':
            h[0] -= 1
        elif d == 'R':
            h[0] += 1
        moveTail(h, t)
        visited.add((t[0], t[1]))
        # print(t)
    return

with open("in.txt") as f:
    for row in f:
        d, s = row.strip().split()
        s = int(s)
        makeMovements(headLoc, tailLoc, d, s)
    print(len(visited))