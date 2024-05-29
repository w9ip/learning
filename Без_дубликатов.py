lst = []
for i in range(int(input())):
    s = input()
    if s in lst:
        continue
    lst.append(s)
print(*lst, sep='\n')
