m, r = float(input()), float(input())

imt = m / (r*r)

if 18.5 <= imt <= 25:
	print('Оптимальная масса')
elif imt < 18.5:
	print('Недостаточная масса')
elif imt > 25:
	print('Избыточная масса')