s = input()
first = s[-4:]
second = s[-8:-5]
third = s[-12:-9]
code = s[:2]
if len(first) == 4 and len(second) == 3 and len(
        third) == 3 and first.isdigit() and second.isdigit() and third.isdigit():
    if len(s) == 14:
        if code == '7-':
            print('YES')
        else:
            print('NO')
    elif len(s) == 12:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
