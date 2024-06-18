nums = [int(e) for e in input().split()]
max_ = nums.pop(0)
total = 0
for n in nums:
    if max_ < n:
        max_ = n
        total += 1
    else:
        max_ = n
print(total)
