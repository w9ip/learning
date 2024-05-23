n = int(input())
counter = 0
while n >= 25:
    counter += 1
    n = n - 25
while n >= 10:
    counter += 1
    n = n - 10
while n >= 5:
    counter += 1
    n = n - 5
while n >= 1:
    counter += 1
    n = n - 1
print(counter)
