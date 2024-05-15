a = int(input())
b = int(input())
op = input()

if op == '+' or op == '-' or op == '*' or op == '/':
    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/':
        if b == 0:
            print('На ноль делить нельзя!')
        else:
            print(a / b)
else:
    print('Неверная операция')
