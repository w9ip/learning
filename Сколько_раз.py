s = input()
star_count = 0
plus_count = 0
for c in s:
    if c == '+':
        plus_count += 1
    elif c == '*':
        star_count += 1
print('Символ + встречается', plus_count, 'раз')
print('Символ * встречается', star_count, 'раз')
