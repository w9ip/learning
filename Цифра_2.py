s = input()
nums = '0123456789'
flag = False
for c in nums:
    if c in s:
        flag = True
        break
if flag:
    print('Цифра')
else:
    print('Цифр нет')
