total = 0
n = int(input())
for i in range(1, n + 1):
    if not n % i:
        total += i
print(total)
