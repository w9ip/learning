glas = 'ауоыиэяюе'
soglas = 'бвгджзйклмнпрстфхцчшщ'
s = input().lower()
glas_count = 0
soglas_count = 0
for c in s:
    for g in glas:
        if g == c:
            glas_count += 1
    for sog in soglas:
        if sog == c:
            soglas_count += 1
print('Количество гласных букв равно', glas_count)
print('Количество согласных букв равно', soglas_count)
