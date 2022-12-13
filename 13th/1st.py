import itertools

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


# Returns 0 if a < b, 1 if a = b, 2 if a > b   
def compare(a, b):
    for i in range(min(len(a), len(b))):
        if isinstance(a[i], int) and isinstance(b[i], int):
            if a[i] > b[i]:
                return 2
            elif a[i] < b[i]:
                return 0
            else:
                continue

        elif isinstance(a[i], int) and isinstance(b[i], list):
            subq = compare([a[i]], b[i])
            if subq == 2:
                return 2
            elif subq == 0:
                return 0
            else:
                continue

        elif isinstance(a[i], list) and isinstance(b[i], int):
            subq = compare(a[i], [b[i]])
            if subq == 2:
                return 2
            elif subq == 0:
                return 0
            else:
                continue

        else:
            subq = compare(a[i], b[i])
            if subq == 2:
                return 2
            elif subq == 0:
                return 0
            else:
                continue
    
    if len(a) < len(b):
        return 0
    elif len(b) == len(a):
        return 1
    else:
        return 2

with open("in.txt") as f:
    indices = []
    for i, (line1,line2, _) in enumerate(itertools.zip_longest(*[f]*3)):
        line1, line2 = [parse(x) for x in [line1, line2]]
        res = compare(line1, line2)
        if res == 0:
            indices.append(i + 1)
    print(sum(indices))


