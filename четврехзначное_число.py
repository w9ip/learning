abcd = int(input())

a = (abcd // 1000)
b = (abcd // 100) % 10
c = (abcd // 10) % 10
d = abcd % 10
print('Цифра в позиции тысяч равна', a)
print('Цифра в позиции сотен равна', b)
print('Цифра в позиции десятков равна', c)
print('Цифра в позиции единиц равна', d)
