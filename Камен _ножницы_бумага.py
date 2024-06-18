timur = input()
ruslan = input()
if timur == ruslan:
    print('ничья')
elif (
        timur == 'камень' and ruslan == 'ножницы'
) or (
        timur == 'бумага' and ruslan == 'камень'
) or (
        timur == 'ножницы' and ruslan == 'бумага'
):
    print('Тимур')
else:
    print('Руслан')
