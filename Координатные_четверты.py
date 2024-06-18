first = []
second = []
third = []
fourth = []
for i in range(int(input())):
    x, y = [int(e) for e in input().split()]
    if x < 0 < y:
        second.append([x, y])
    elif x > 0 and y > 0:
        first.append([x, y])
    elif x < 0 and y < 0:
        third.append([x, y])
    elif x > 0 > y:
        fourth.append([x, y])
print('Первая четверть:', len(first))
print('Вторая четверть:', len(second))
print('Третья четверть:', len(third))
print('Четвертая четверть:', len(fourth))
