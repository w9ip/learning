n = int(input())
lst = []
for i in range(n):
    num = int(input())
    if i & 1:
        continue
    lst.append(num)
print(lst)
