n = int(input())
lst = []
for i in range(n):
    num = int(input())
    print(num)
    lst.append(num ** 2 + 2 * num + 1)
print()
print(*lst, sep='\n')
