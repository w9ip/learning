d = dict()
n = int(input())
for _ in range(n):
    inp = input().split()
    d[inp[0]] = inp[1]
w = input()
print(d[w] if w in d else dict(map(lambda x: x[::-1], d.items()))[w])
