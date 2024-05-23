n, m = int(input()), int(input())

for i in range(n, m + 1):
    if (not i % 17) or (i % 10 == 9) or (not i % 3 and not i % 5):
        print(i)
