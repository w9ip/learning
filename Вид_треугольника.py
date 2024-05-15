b = int(input())
c = int(input())
a = int(input())

if a == b == c:
    print('Равносторонний')
elif a == b != c or a == c != b or b == c != a:
    print('Равнобедренный')
else:
    print('Разносторонний')
