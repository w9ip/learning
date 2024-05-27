n = int(input())
res = ''
while n > 0:
    if n % 2 == 0:
        res += '0'
    else:
        res += '1'
    n //= 2
for i in range(len(res) - 1, -1, -1):
    print(res[i], end='')
