
children = {'/': []}
pwd = '/'
folderSize = {}

# Idea, log all the children, and all the filesizes. Once the 
# input has been fully parsed, run a quick recursive traversal and find
# size of all the folders instead, then do the math.

with open("in.txt") as f:
    for row in f:
        # print(pwd, children)
        row = row.strip().split(' ')

        if row[0] == '$':
            if row[1] == 'cd':
                if row[2] == "..":
                    add = pwd.split('|')
                    add.pop()
                    pwd = '|'.join(add)

                elif row[2] == '/':
                    continue

                else:
                    pwd += '|' + row[2]

            elif row[1] == 'ls':
                continue

        else:
            if pwd not in children:
                children[pwd] = []

            if row[0] == 'dir':
                child = pwd + '|' + row[1]
                children[pwd].append(child)
            
            else:
                size = int(row[0])
                filename = pwd + "|" + row[1]
                if pwd not in folderSize:
                    folderSize[pwd] = 0
                folderSize[pwd] += size

calculatedSizes = {}

def recurse(root):
    total = 0
    if root in children:
        kids = children[root]
        total += sum([recurse(x) for x in kids])
    
    if root in folderSize:
        total += folderSize[root]
    
    calculatedSizes[root] = total
    return total

recurse("/")    
total = 0
for _, v in calculatedSizes.items():
    if v <= 100000:
        total += v
print(total) 
        
                


        
