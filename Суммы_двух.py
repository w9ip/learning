n = int(input())
lst = []
tmp = int(input())
for _ in range(n-1):
    num = int(input())
    lst.append(num + tmp)
    tmp = num
print(lst)
