qty = int(input())
cds = [input() for e in range(qty)]
for cd in cds:
    f, n, o, d, m, y = cd.split(',')
    # подсчет кол-ва различных символов в ФИО (регистр важен)
    len_uniq_fio = len(set(f+n+o))

    # берется сумма цифр в дне и месяце рождения и умножается на 64
    sum_d_m = sum(int(e) for e in tuple(d+m)) * 64

    # Для первой (по позиции в слове) буквы фамилии
    # определяется её номер в алфавите (в 1-индексации),
    # умноженный на 256 (регистр буквы не важен).
    s_idx = ord(f[0].lower()) - 96

    res = hex(len_uniq_fio + sum_d_m + s_idx * 256).upper()[-3:]
    print(res, end=' ')