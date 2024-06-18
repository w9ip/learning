n = int(input())
quarantine = []
target = 'anton'
initial = ''
for i in range(n):
    refrigerator = input()
    for c in target:
        found = refrigerator.find(c)
        initial += refrigerator[found]
        refrigerator = refrigerator[found+1:]
    if initial == target:
        quarantine.append(i + 1)
    initial = ''

print(*quarantine)
