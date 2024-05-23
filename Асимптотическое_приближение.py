from math import log

n = int(input())
total = 1
for i in range(2, n + 1):
    total += 1 / i
print(total - log(n))
