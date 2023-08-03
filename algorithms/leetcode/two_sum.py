def t(nums, target):
    d = {}
    for i, v in enumerate(nums):
        x = target - v
        if v not in d:
            d[v] = i
        if x in d and d[x] != i:
            return [d[x], i]
    else:
        return []


print(t([2, 7, 11, 15], 9))  # [0, 1]
print(t([3, 2, 4], 6))  # [1, 2]
print(t([3, 3], 6))  # [0, 1]
print(t([3, 4, 6, 7, 10, 3], 13))  # [0, 1]
