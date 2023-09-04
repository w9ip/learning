# from random import shuffle
#
# rockets_logs = [['50', '7', '25', '3632', 'A'], ['14', '23', '52', '212372', 'S'], ['15', '0', '5', '3632', 'C'],
#                 ['14', '21', '30', '212372', 'A'], ['50', '7', '26', '3632', 'C'], ['14', '21', '30', '3632', 'A'],
#                 ['14', '21', '40', '212372', 'B'], ['14', '23', '52', '3632', 'B']]
# shuffle(rockets_logs)

sort_logs = {}
rockets_logs = [input().split() for _ in range(int(input()))]
for day, hour, minute, id, status in rockets_logs:
    l = int(day), int(hour), int(minute), status
    sort_logs.setdefault(int(id), []).append(l)

for rocket in sort_logs:
    sort_logs[rocket].sort()

abcs_sorted = {}
for rocket_id, rocket_log in sort_logs.items():
    stack = []
    key = ''
    for log in rocket_log:
        log_minutes = int(log[0]) * 24 * 60 + int(log[1]) * 60 + int(log[2])
        if log[-1] not in 'CS':
            stack.append(log_minutes)
            key += log[-1]
        else:
            key += log[-1]
            stack.append(log_minutes)
            abcs_sorted.setdefault(rocket_id, {})
            abcs_sorted[rocket_id][key] = stack[:]
            if key == 'ABC':
                res = (stack[1]-stack[0]) + (stack[2] - stack[1])
                abcs_sorted[rocket_id][key] = res
            elif key == 'ABS':
                res = (stack[1] - stack[0]) + (stack[2] - stack[1])
                abcs_sorted[rocket_id][key] = res
            elif key == 'AC':
                res = stack[1] - stack[0]
                abcs_sorted[rocket_id][key] = res
            stack.clear()
            key = ''

res = [sum(abcs_sorted[e].values()) for e in sorted(abcs_sorted.keys())]
print(*res)
