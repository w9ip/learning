def quick_merge(list1, list2):
    result = []

    p1 = 0
    p2 = 0

    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1
    if p1 < len(list1):
        result += list1[p1:]
    else:
        result += list2[p2:]

    return result


n = int(input())
first = [int(e) for e in input().split()]
for i in range(n - 1):
    second = [int(e) for e in input().split()]
    first = quick_merge(first, second)
print(*first)
