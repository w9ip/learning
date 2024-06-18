lst = []
for _ in range(int(input())):
    lst.append(int(input()))
compare = int(input())
for i in range(len(lst)):
    flag = False
    for j in range(len(lst)):
        if i == j:
            continue
        if lst[i] * lst[j] == compare:
            print('ДА')
            flag = True
            break
    if flag:
        break
else:
    print('НЕТ')
