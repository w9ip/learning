print(*[int(e) ** 2 for e in input().split() if int(e) % 2 == 0 and (int(e) ** 2) % 10 != 4])
