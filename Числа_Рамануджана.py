find = 0
for a in range(1, 33):
    for b in range(1, 33):
        for c in range(1, 33):
            for d in range(1, 33):
                if a != d != b != c:
                    if a ** 3 + b ** 3 == d ** 3 + c ** 3:
                        if find != a ** 3 + b ** 3:
                            find = a ** 3 + b ** 3
                            print(find)
