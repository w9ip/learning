nums = [int(e) for e in input().split()]
different = nums[0]
total = 1
for i in range(1, len(nums)):
    if nums[i] > different:
        different = nums[i]
        total += 1
print(total)