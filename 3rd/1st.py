score = 0

def convert(c):
    if str.islower(c):
        return ord(c) - 96
    else:
        return ord(c) - 38

with open("in.txt") as f:
    for row in f:
        fh, sh = row[:len(row) // 2] , row[len(row) // 2:]
        fs = set(list(fh))
        for c in sh:
            if c in fs:
                score += convert(c)
                break
    print(score)
        

