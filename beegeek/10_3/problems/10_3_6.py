s = input().split()

result = []

for w in s:
    x = result.count(w)
    print(w if x < 1 else f'{w}_{x}', end=' ')
    result.append(w)
