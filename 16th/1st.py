from collections import deque
import time

startime = time.time()

graph = {}
press = {}
fw = [] # For running Floyd-Warshall Algorithm
mapping = {} # Mapping from the stupid letters to idx

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
def dfs(node, time, valves):
    if valves <= 0 or time <= 0:
        return 0
    
    else:
        # print(node, time)
        if press[node] == 0:
            nidx = mapping[node]
            nodes = [x for x, idx in mapping.items() if valves & (1 << idx)]
            res = [dfs(x, time - fw[nidx][mapping[x]], valves) for x in nodes]
            if len(res) == 0:
                return 0
                
            return max(res)

        else:
            pVal = press[node] * (time - 1)
            nidx = mapping[node]
            valves = valves - (1 << nidx)
            nodes = [x for x, idx in mapping.items() if valves & (1 << idx)]
            res = [dfs(x, time - 1 - fw[nidx][mapping[x]], valves) for x in nodes]
            if len(res) == 0:
                return pVal
                
            return max(res) + pVal

print(dfs('AA', 30, bitmask))
print(time.time() - startime)

    

