score = 0
with open("in.txt") as f:
    for row in f:
        rA, rB = row.split(",")
        lA, rA = rA.split('-')
        lB, rB = rB.split('-')
        lA, rA, lB, rB = map(lambda x: int(x), [lA, rA, lB, rB])
        if (lA >= lB and rA <= rB) or(lA <= lB and rA >= rB):
            score += 1
    print(score)
