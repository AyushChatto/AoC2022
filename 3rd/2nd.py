score = 0

def convert(c):
    if str.islower(c):
        return ord(c) - 96
    else:
        return ord(c) - 38

with open("in.txt") as f:
    rows = [row for row in f]
    for i in range(0, len(rows), 3):
        a, b, c = rows[i:i+3]
        sa, sb = set(list(a)), set(list(b))
        for char in c:
            if char in sa and char in sb:
                score += convert(char)
                break
    print(score)
        
        

