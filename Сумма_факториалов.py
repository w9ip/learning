from math import factorial

n = int(input())
total = 0
for i in range(1, n + 1):
    total += factorial(i)
print(total)
