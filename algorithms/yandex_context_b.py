from bisect import insort

N = int(input())

rockets_logs = [
    input().split() for e in range(N)
]

sorted_logs = {}

for day, hour, minute, id, status in rockets_logs:
    lst = (day, hour, minute, status)
    sorted_logs.setdefault(id, [])
    insort(sorted_logs[id], lst)


def calculate_interval(date1, date2):
    day1, hour1, minute1 = date1
    day2, hour2, minute2 = date2


for rocket, logs in sorted_logs.items():
    A, B, C, S = 0, 0, 0, 0
    flag = 0
    rocket_sum_minute = 0
    for day, hour, minute, status in logs:
        print(day, hour, minute, status)
        if status == 'A':
            A = day, hour, minute, status
        if status == 'B':
            B = day, hour, minute, status
        if status == 'C':
            C = day, hour, minute, status
            flag = 1
        if status == 'S':
            S = day, hour, minute, status
            flag = 1
        if flag:
            if A and B and C:
                print(f'A={A}, B={B}, C={C}')
            elif A and C:
                print(f'A={A}, C={C}')
            elif A and B and S:
                print(f'A={A}, B={B}, S={S}')
            flag = 0
            A, B, C, S = 0, 0, 0, 0
