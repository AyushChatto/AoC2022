from collections import deque 

blueprints = {}
maxes = {}
timeLimit = 24

with open("in.txt") as f:
    for idx, row in enumerate(f):
        nums = tuple([int(x) for x in row.strip().split(' ') if x.isnumeric()])
        blueprints[idx + 1] = nums
        maxes[idx + 1] = [
            max(nums[0], nums[1], nums[2], nums[4]),
            nums[3],
            nums[5]
        ]
        #b[0] = cost of or (ore)
        #b[1] = cost of cr (ore)
        #b[2], b[3] = cost of br (ore, clay)
        #b[4], b[5] = cost of gr (ore, obsidian)

dp = {}
# 9-tuple = (time, o, c, b, g, or, cr, br, gr)
t = 0
o = 1
c = 2
b = 3
g = 4
oR = 5
cR = 6
bR = 7
gR = 8

intial = [24, 0, 0, 0, 0, 1, 0, 0, 0]
cb = 0
cmax = 0

def recurse(node):
    tn = tuple(node)
    if node[t] == 0:
        dp[tn] = node[g]
        return node[g]

    elif tn in dp:
        return dp[tn]
    
    else:
        ans = []
        temp = node[:]
        temp[t] -= 1
        temp[o] += node[oR]
        temp[c] += node[cR]
        temp[b] += node[bR]
        temp[g] += node[gR]

        if node[o] < cmax[0] or node[c] < cmax[1] or node[b] < cmax[2]:
            ans.append(recurse(temp))

        # If enough ore to make an ore-robot, and not enough ore-robots
        if node[o] >= cb[0] and node[oR] < cmax[0]:
            temp1 = temp[:]
            temp1[o] -= cb[0]
            temp1[oR] += 1
            ans.append(recurse(temp1))

        # Enough ore to make clay robot and not enough clay robots
        if node[o] >= cb[1] and node[cR] < cmax[1]:
            temp2 = temp[:]
            temp2[o] -= cb[1]
            temp2[cR] += 1
            ans.append(recurse(temp2))

        # Enough ore and clay to make obsidian robots, and not enough obsidian robots
        if node[o] >= cb[2] and node[c] >= cb[3] and node[bR] <= cmax[2]:
            temp3 = temp[:]
            temp3[o] -= cb[2]
            temp3[c] -= cb[3]
            temp3[bR] += 1
            ans.append(recurse(temp3))

        # Enough ore and oBsidian to make geode robots
        if node[o] >= cb[4] and node[b] >= cb[5]:
            temp4 = temp[:]
            temp4[o] -= cb[4]
            temp4[b] -= cb[5]
            temp4[gR] += 1
            ans.append(recurse(temp4))

        res = max(ans)
        dp[tn] = res
        return res

cumsum = 0  
for i in blueprints:
    dp = {}
    cb = blueprints[i]
    cmax = maxes[i]
    ans = recurse(intial)
    print(ans, i * ans)
    cumsum += i * ans
print(cumsum)






