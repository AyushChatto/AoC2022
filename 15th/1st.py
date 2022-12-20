
noBeacon = set()

def addRange(s, b, ty):
    dy = abs(s[1] - b[1])
    dx = abs(s[0] - b[0])
    md = dy + dx
    xSurplus = md - abs(s[1] - ty)
    if xSurplus <= 0:
        return
    noBeacon.add((s[0] - xSurplus, s[0] + xSurplus))
    return (s[0] - xSurplus, s[0] + xSurplus)


def merge():
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
            elif l <= r1 and l1 <= l:
                rSet.add((l1, r1))
                rSet.add((l, r))
                aSet.add((l1, r))
                l = l1

            elif r <= r1 and l1 <= r:
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
        merge()
    return

file = "in.txt"
target = 10 if file == 'test.txt' else 2000000
with open(file) as f:
    for row in f:
        row = row.strip().split(' ')
        sensor = row[2:4]
        beacon = row[8:]
        sensor = [int(x[2:-1]) for x in sensor]
        beacon[0] = int(beacon[0][2:-1])
        beacon[1] = int(beacon[1][2:])
        newVal = addRange(sensor, beacon, target)
        if newVal:        
            merge()
    
    count = 0
    for i, j in noBeacon:
        count += (j - i)
    print(count)

        
        
        

        