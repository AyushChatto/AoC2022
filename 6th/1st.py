from collections import deque 

with open("in.txt") as f:
    for row in f:
        window = deque([x for x in row[:3]])
        for i, c in enumerate(row[3:]):
            window.append(c)
            # print(window, i)
            if len(window) == len(set(window)):
                print(i + 4)
                break
            window.popleft()

