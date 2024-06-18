n = int(input())
for i in range(n):
    row = [int(e) for e in input().split()]
    res = [e for e in row if e > sum(row) / len(row)]
    print(len(res))
