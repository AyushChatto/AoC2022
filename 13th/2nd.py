from functools import cmp_to_key

def parse(s):
    ans = []
    num = ""
    stack = [ans]
    for c in s:
        if c == '[':
            newArr = []
            stack[-1].append(newArr)
            stack.append(newArr)
            

        elif c == ']':
            if num.isnumeric():
                stack[-1].append(int(num))
                num = ""
            stack.pop()

        elif c == ',':
            if num.isnumeric():
                stack[-1].append(int(num))
                num = ""

        else:
            num += c

    return ans[0]


# Returns -1 if a < b, 0 if a = b, 1 if a > b   
def compare(a, b):
    for i in range(min(len(a), len(b))):
        if isinstance(a[i], int) and isinstance(b[i], int):
            if a[i] > b[i]:
                return 1
            elif a[i] < b[i]:
                return -1
            else:
                continue

        elif isinstance(a[i], int) and isinstance(b[i], list):
            subq = compare([a[i]], b[i])
            if subq == 1:
                return 1
            elif subq == -1:
                return -1
            else:
                continue

        elif isinstance(a[i], list) and isinstance(b[i], int):
            subq = compare(a[i], [b[i]])
            if subq == 1:
                return 1
            elif subq == -1:
                return -1
            else:
                continue

        else:
            subq = compare(a[i], b[i])
            if subq == 1:
                return 1
            elif subq == -1:
                return -1
            else:
                continue
    
    if len(a) < len(b):
        return -1
    elif len(b) == len(a):
        return 0
    else:
        return 1

lines = [[2], [6]]
with open("in.txt") as f:
    for line in f:
        line = line.strip()

        if line != "":
            line = parse(line)
            lines.append(line)

lines = sorted(lines, key=cmp_to_key(compare))
print((lines.index([2]) + 1) * (lines.index([6]) + 1))
