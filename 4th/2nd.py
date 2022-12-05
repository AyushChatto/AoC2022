score = 0

def overlap(la, ra, lb, rb):
    return not ((rb < la) or (ra < lb))

with open("in.txt") as f:
    for row in f:
        rA, rB = row.split(",")
        lA, rA = rA.split('-')
        lB, rB = rB.split('-')
        lA, rA, lB, rB = map(lambda x: int(x), [lA, rA, lB, rB])
        if overlap(lA, rA, lB, rB):
            score += 1
    print(score)
