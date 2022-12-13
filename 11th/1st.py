
items = {}
operation = {} # Stored as a tuple (op, val, val)
tests = {} # Stored as a tuple (divisor, trueTarget, falseTarget)

with open("in.txt") as f:
    currMonkey = 0
    divisor = 0
    trueTarget = 0
    falseTarget = 0

    for row in f:
        row = row.strip().split(' ')
        if row[0] == 'Monkey':
            currMonkey = int(row[1].replace(":", ""))

        elif row[0] == 'Starting':
            items[currMonkey] = [int(x.replace(",", "")) for x in row[2:]]
        
        elif row[0] == 'Operation:':
            a, op, b = row[-3:]
            a = int(a) if a != 'old' else 'old'
            b = int(b) if b != 'old' else 'old'
            operation[currMonkey] = (op, a, b)

        elif row[0] == 'Test:':
            divisor = int(row[-1])
        
        elif row[0] == 'If' and row[1] =='true:':
            trueTarget = int(row[-1])
        
        elif row[0] == 'If' and row[1] == 'false:':
            falseTarget = int(row[-1])
            tests[currMonkey] = (divisor, trueTarget, falseTarget)
            trueTarget, falseTarget, divisor = 0, 0, 0

    numMonkey = currMonkey
    inspectCount = {}
    for i in range(20):
        for m in range(numMonkey + 1):
            if m not in inspectCount:
                inspectCount[m] = 0
            
            divisor, trueT, falseT = tests[m]
            it = items[m]
            items[m] = []

            for item in it:
                op, valA, valB = operation[m]
                inspectCount[m] += 1
                valA = item if valA != 'old' else item
                valB = valB if valB != 'old' else item
                worry = valA * valB if op == '*' else valA + valB
                worry //= 3

                if worry % divisor == 0:
                    items[trueT].append(worry)
                else:
                    items[falseT].append(worry)

    vs = sorted(inspectCount.values())
    print(vs[-1] * vs[-2])
    

