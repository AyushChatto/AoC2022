monkey = {} # name -> number or (monkey, monkey, operation)

with open("in.txt") as f:
    for row in f:
        row = row.strip().split()
        mName = row[0][:-1]
        if row[1].isnumeric():
            monkey[mName] = int(row[1])
        else:
            monkey[mName] = (row[1], row[3], row[2])

def solve(m):
    v = monkey[m]
    if isinstance(v, int):
        return v
    else:
        m1, m2, op = v
        if op == "+":
            ans = solve(m1) + solve(m2)
        elif op == "-":
            ans = solve(m1) - solve(m2)
        elif op == "*":
            ans = solve(m1) * solve(m2)
        elif op == "/":
            ans = solve(m1) // solve(m2)
        monkey[m] = ans
        return ans
print(solve("root"))


