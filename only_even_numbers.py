counter = 0
for i in range(10):
    n = int(input())
    if not n & 1:
        counter += 1
print('YES' if counter == 10 else 'NO')
