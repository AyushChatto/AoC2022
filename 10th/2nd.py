
x = 1
clock = 0
currRow = ""
currIndex = 0

def sprite():
    return range(x - 1, x + 2)

with open("in.txt") as f:
    for row in f:
        row = row.strip().split(' ')

        if row[0] == "noop":
            clock += 1
            currRow += "#" if currIndex in sprite() else "."
            currIndex += 1

        elif row[0] == "addx":
            clock += 1
            currRow += "#" if currIndex in sprite() else "."
            currIndex += 1

            if clock % 40 == 0:
                print(currRow)
                currRow = ""
                currIndex = 0

            clock += 1
            currRow += "#" if currIndex in sprite() else "."
            currIndex += 1

            x += int(row[1])

        if clock % 40 == 0:
            print(currRow)
            currRow = ""
            currIndex = 0
