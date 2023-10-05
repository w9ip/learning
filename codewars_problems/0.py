from collections import Counter


def stray(arr):
    return Counter(arr).most_common()[-1][0]


print(stray([17, 17, 3, 17, 17, 17, 17]))
print(stray([2, 2, 2, 1]))
