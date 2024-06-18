nums = [int(e) for e in input().split()]
print(*[nums[-1]] + nums[:-1])
