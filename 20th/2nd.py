
nums = []
with open('in.txt') as f:
    for i, row in enumerate(f):
        num = int(row) * 811589153
        nums.append((num, i))

final = nums[:]
for j in range(10):
    for i in nums:
        ind = final.index(i)
        shift = i[0]
        newInd = (ind + shift) % (len(nums) - 1)
        if newInd != 0:
            final.pop(ind)
            final.insert(newInd, i)
        else:
            final.pop(ind)
            final.append(i)

final = [x[0] for x in final]
ind = final.index(0)
thousandth = final[(ind + 1000) % len(nums)]
twothousandth = final[(ind + 2000) % len(nums)]
threethousandth = final[(ind + 3000) % len(nums)]
print(thousandth + twothousandth + threethousandth)