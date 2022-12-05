from collections import deque

readingStack = True
readingBlank = False

stacks = {}
maxCol = 0

with open("in.txt") as f:
    for row in f:
        if readingStack:
            if row[1].isnumeric():
                readingStack = False
                readingBlank = True
                maxCol = max([int(x) for x in row.split(' ') if x.isnumeric()])
            
            else:
                for i in range(0, len(row), 4):
                    if row[i + 1] == ' ':
                        continue
                    else:
                        column = (i // 4) + 1
                        if column not in stacks:
                            stacks[column] = []
                        stacks[column].append(row[i + 1])
                
        
        elif readingBlank:
            readingBlank = False
            newStack = [deque([])] * maxCol
            for k, v in stacks.items():
                newStack[k - 1] = deque(v)
            stacks = newStack
            continue
        
        else:
            inst = row.strip().split(' ')
            num, source, dest = map(lambda x: int(x), [inst[1], inst[3], inst[5]])
            source -=1
            dest -= 1
            for _ in range(num):
                val = stacks[source].popleft()
                stacks[dest].appendleft(val)
    print(''.join([x[0] for x in stacks]))
        
            



        