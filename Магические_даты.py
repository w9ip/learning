def is_magic(date):
  date = date.split(".")
  if int(date[0]) * int(date[1]) == int(date[2]) % 100:
    return True
  return False
  
# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))