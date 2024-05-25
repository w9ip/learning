n = int(input())
smallest = n
for i in range(2, n + 1):
    compare = n % i
    if not compare and i < smallest:
        smallest = i
        break
print(smallest)
