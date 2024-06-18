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
) or (
        timur == 'Спок' and ruslan == 'ножницы'
) or (
        timur == 'ножницы' and ruslan == 'ящерица'
) or (
        timur == 'ящерица' and ruslan == 'бумага'
) or (
        timur == 'бумага' and ruslan == 'Спок'
) or (

        timur == 'Спок' and ruslan == 'камень'
) or (
        timur == 'ящерица' and ruslan == 'Спок'
) or (
        timur == 'камень' and ruslan == 'ящерица'
):
    print('Тимур')
else:
    print('Руслан')
