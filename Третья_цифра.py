n = int(input())
while n // 1000 != 0:
    n //= 10
print(n%10)
