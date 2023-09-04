rockets_logs = [input().split() for _ in range(int(input()))]
sorted_logs = {}
for day, hour, minute, id, status in rockets_logs:
    id = int(id)
    sorted_logs.setdefault(id, []).append((int(day)*24*60+int(hour)*60+int(minute), status))
res_dir = {}
for rocket, logs in sorted_logs.items():
    logs.sort()
    A, B, C, S = 0, 0, 0, 0
    flag = 0
    rocket_sum_minute = 0
    for minutes, status in logs:
        if status == 'A':
            A = minutes
        if status == 'B':
            B = minutes
        if status == 'C':
            C = minutes
            flag = 1
        if status == 'S':
            S = minutes
            flag = 1
        if flag:
            if A and B and C:
                rocket_sum_minute += (C-B) + (B-A)
            elif A and C:
                rocket_sum_minute += (C-A)
            elif A and B and S:
                rocket_sum_minute += (S - B) + (B - A)
            flag = 0
            A, B, C, S = 0, 0, 0, 0
    res_dir.setdefault(rocket, rocket_sum_minute)
print(*(res_dir[e] for e in sorted(res_dir.keys())))

