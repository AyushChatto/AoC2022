from collections import deque
import time

startime = time.time()

graph = {}
press = {}
fw = [] # For running Floyd-Warshall Algorithm
mapping = {} # Mapping from the stupid letters to idx
c = [0]

with open("in.txt") as f:
    for row in f:
        row = row.strip().split(' ')
        source = row[1]
        p = int(row[4].strip().split('=')[1][:-1])
        press[source] = p
        destinations = row[9:]
        destinations = [x.replace(',', '') for x in destinations]
        graph[source] = destinations

fw = [10**5] * len(graph)
for idx, item in enumerate(graph):
    mapping[item] = idx
    fw[idx] = [10**5] * len(graph)

for s, ds in graph.items():
    sidx = mapping[s]
    for d in ds:
        didx = mapping[d]
        fw[sidx][didx] = 1

for kx in graph:
    for ix in graph:
        for jx in graph:
            i, j, k = mapping[ix], mapping[jx], mapping[kx]
            if fw[i][j] > fw[i][k] + fw[k][j]:
                fw[i][j] = fw[i][k] + fw[k][j]

bitmask = 0

for n, p in press.items():
    if p == 0:
        continue
    
    idx = 1 << mapping[n]
    bitmask = bitmask | idx 

# print(bin(bitmask))
# for i in fw:
#     print(i)
# print()

# Now, run a DFS from AA to all the nodes with a sealed valve with value
def dfs(node, ele, time, etime, valves):
    c[0] += 1
    if c[0] % 10**5 == 0:
        print(c[0])

    if valves <= 0 or (time <= 0 and etime <= 0):
        return 0
    
    else:
        # print(node, ele, time, etime, bin(valves))
        if press[node] == 0 and press[ele] == 0: #Start condition
            nidx = mapping[node]
            eidx = mapping[ele]
            
            nodes = [x for x, idx in mapping.items() if valves & (1 << idx)]
            res = [dfs(x, y, time - fw[nidx][mapping[x]], etime - fw[eidx][mapping[y]], valves) for x in nodes for y in nodes if x < y]
            return max(res)

        elif time <= 0 and etime > 0 : #Only elephant can move
            eVal = press[ele] * (etime - 1)
            eidx = mapping[ele]
            valves = valves - (1 << eidx)
            nodes = [x for x, idx in mapping.items() if valves & (1 << idx)]
            res = [dfs(node, y, time, etime - 1 - fw[eidx][mapping[y]], valves) for y in nodes if etime - 1 - fw[eidx][mapping[y]] >= 0]
            if len(res) == 0:
                return eVal
                
            return max(res) + eVal

        elif time > 0 and etime <= 0: #Only I can move
            pVal = press[node] * (time - 1)
            nidx = mapping[node]
            valves = valves - (1 << nidx)
            nodes = [x for x, idx in mapping.items() if valves & (1 << idx)]
            res = [dfs(x, ele, time - 1 - fw[nidx][mapping[x]], etime, valves) for x in nodes if time - 1 - fw[nidx][mapping[x]] >= 0]
            if len(res) == 0:
                return pVal
                
            return max(res) + pVal

        else: #Both of us can move
            pVal = press[node] * (time - 1)
            eVal = press[ele] * (etime - 1)
            nidx = mapping[node]
            eidx = mapping[ele]
            valves = valves - (1 << nidx)
            valves = valves - (1 << eidx)
            nodes = [x for x, idx in mapping.items() if valves & (1 << idx)]
            res = [dfs(x, y, time - 1 - fw[nidx][mapping[x]], etime - 1 - fw[eidx][mapping[y]], valves) for x in nodes for y in nodes if y != x and (time - 1 - fw[nidx][mapping[x]] >= 0) and (etime - 1 - fw[eidx][mapping[y]] >= 0)]
            if len(res) == 0:
                return pVal + eVal
                
            return max(res) + pVal + eVal

print(dfs('AA', 'AA', 26, 26, bitmask))
print(time.time() - startime)

    

