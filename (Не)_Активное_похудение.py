# 60 дней до лета
# Дни пронумерованы 1 - 60
# Достичь до начала лета, планку <= 88кг
# Решено худеть на одну и ту же массу ежедневно
day = int(input())
current_weight = float(input())
aim = 100 - 0.2 * day
if current_weight > aim:
    print('Что-то пошло не так')
    print(f'#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {current_weight} кг, ЦЕЛЬ по ВЕСУ = {aim} кг')
else:
    print('Все идет по плану')
    print(f'#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {current_weight} кг, ЦЕЛЬ по ВЕСУ = {aim} кг')
