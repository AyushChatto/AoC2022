monkey = {} # name -> number or (monkey, monkey, operation)

with open("in.txt") as f:
    for row in f:
        row = row.strip().split()
        mName = row[0][:-1]
        if mName == "humn":
            monkey[mName] = None
        elif mName == "root":
            monkey[mName] = (row[1], row[3], "=")
        elif row[1].isnumeric():
            monkey[mName] = int(row[1])
        else:
            monkey[mName] = (row[1], row[3], row[2])

# Solve as much as possible
def solve(m):
    v = monkey[m]
    if isinstance(v, int) or v == None:
        return v
    
    else:
        m1, m2, op = v
        
        a1 = solve(m1)
        a2 = solve(m2)
        if a1 == None or a2 == None or op == "=":
            return None
        elif op == "+":
            ans =  a1 + a2
        elif op == "-":
            ans = a1 - a2
        elif op == "*":
            ans = a1 * a2
        elif op == "/":
            ans = a1 // a2
        monkey[m] = ans
        return ans

def invert(m, v):
    if monkey[m] == None:
        monkey[m] = v
        return v

    m1, m2, op = monkey[m]
    didFlip = False
    if isinstance(monkey[m2], int):
        m2, m1 = m1, m2
        didFlip = True
    # m1 is known, monkey[m] should be v
    monkey[m] = v
    ans = None
    if op == "=":
        ans =invert(m2, monkey[m1])
    elif op == "+":
        ans =invert(m2, monkey[m] - monkey[m1])
    elif op == "-":
        if didFlip:
            ans =invert(m2, monkey[m] + monkey[m1])
        else:
            ans =invert(m2, monkey[m1] - monkey[m])

    elif op == "*":
        ans =invert(m2, monkey[m] // monkey[m1])

    elif op == "/":
        if didFlip:
            ans =invert(m2, monkey[m] * monkey[m1])
        else:
            ans =invert(m2, monkey[m1] // monkey[m])
    return ans
    
solve("root")

r1 = monkey["root"][0]
r2 = monkey["root"][1]
if isinstance(monkey[r2], int):
    r2, r1 = r1, r2
ans = invert("root", monkey[r1])
print(ans)
# print(monkey)



