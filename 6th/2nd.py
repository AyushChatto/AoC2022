from collections import deque 

with open("in.txt") as f:
    for row in f:
        window = deque([x for x in row[:13]])
        for i, c in enumerate(row[13:]):
            window.append(c)
            # print(window, i)
            if len(window) == len(set(window)):
                print(i + 14)
                break
            window.popleft()

