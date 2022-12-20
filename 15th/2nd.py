import time
startTime = time.time()

file = "in.txt"
target = 20 if file == 'test.txt' else 4000000

diamonds = []

def addRange(s, b, ty):
    x, y = s
    dy = abs(s[1] - b[1])
    dx = abs(s[0] - b[0])
    md = dy + dx
    top = (x, max(y - md, 0))
    bottom = (x, min(y + md, ty))
    left = (max(x - md, 0), y)
    right = (min(x + md, ty), y)
    diamonds.append((tuple(s), md, top, bottom, left, right))
    return   

def merge(noBeacon):
    rSet = set()
    aSet = set()

    for newVal in noBeacon:
        l, r = newVal
        for (l1, r1) in noBeacon:
            if (l1, r1) == newVal:
                continue

            # superset
            if l <= l1 and r >= r1:
                rSet.add((l1, r1))

            elif l1 <= l and r1 >= r:
                rSet.add((l, r))

            # intersect
            elif (l <= r1 and l1 <= l) or (l - r1 == 1):
                rSet.add((l1, r1))
                rSet.add((l, r))
                aSet.add((l1, r))
                l = l1

            elif (r <= r1 and l1 <= r) or (l1 - r == 1):
                rSet.add((l1, r1))
                rSet.add((l, r))
                aSet.add((l, r1))
                r = r1

    for s in rSet:
        if s in noBeacon:
            noBeacon.remove(s)

    flag = False
    for a in aSet:
        if a not in noBeacon:
            noBeacon.add(a)
            flag = True
    
    if flag:
        merge(noBeacon)
    return

def occupato(diamond, row):
    s, md, t, b, _, _ = diamond
    if row < t[1] or row > b[1]:
        return None
    
    else:
        dy = abs(s[1] - row)
        dx = md - dy
        if dx < 0:
            return None
        else:
            return ( max(s[0] - dx, 0), min(s[0] + dx, target))


with open(file) as f:
    for row in f:
        row = row.strip().split(' ')
        sensor = row[2:4]
        beacon = row[8:]
        sensor = [int(x[2:-1]) for x in sensor]
        beacon[0] = int(beacon[0][2:-1])
        beacon[1] = int(beacon[1][2:])
        addRange(sensor, beacon, target)
    
    for i in range(target):
        if i % 100000 == 0:
            print(i)

        ranges = [occupato(x, i) for x in diamonds]
        noX = set(ranges)
        if None in noX:
            noX.remove(None)

        # print(i, noX)
        merge(noX)
        if len(noX) > 1:
            a, b = list(noX)
            if a[0] > b[0]:
                a, b = b, a
            x = b[0] - 1
            ans = (x * (4*10**6)) + i
            print(ans)
            print(time.time() - startTime)
            break
        # print(i, noX)
        # print()




    

        
        

        