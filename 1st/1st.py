values = []
cValue = 0
with open("1stin.txt") as f:
    for row in f:
        if row == "\n":
            values.append(cValue)
            cValue = 0
        else:
            cValue += int(row)

print(max(values))
