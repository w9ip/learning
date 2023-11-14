info = dict(name='bob', age=25)

name1 = info.setdefault('name')  # Параметр default не задан
name2 = info.setdefault('name', 'Max')  # Параметр default задан

print(name1)
print(name2)
