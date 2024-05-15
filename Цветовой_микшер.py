c1 = input()
c2 = input()

if c1 == 'красный' and c2 == 'синий':
    print('фиолетовый')
elif c1 == 'красный' and c2 == 'желтый':
    print('оранжевый')
elif c1 == 'синий' and c2 == 'желтый':
    print('зеленый')
elif c2 == 'красный' and c1 == 'синий':
    print('фиолетовый')
elif c2 == 'красный' and c1 == 'желтый':
    print('оранжевый')
elif c2 == 'синий' and c1 == 'желтый':
    print('зеленый')
elif c1 == 'красный' and c2 == 'красный':
    print('красный')
elif c1 == 'синий' and c2 == 'синий':
    print('синий')
elif c1 == 'желтый' and c2 == 'желтый':
    print('желтый')
else:
    print('ошибка цвета')